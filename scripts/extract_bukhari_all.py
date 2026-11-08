"""
scripts/extract_bukhari_all.py
ETL pipeline for Sahih al-Bukhari:
1. Downloads and archives full-text editions (Arabic vocalized, Arabic plain, English, Nusantara/Indonesian) into data/editions/.
2. Harmonizes and compiles all 97 books into canonical data/hadiths/{book_id}.json.
3. Updates data/books.json and data/chapters/{book_id}.json with accurate ranges.
"""

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
EDITIONS_DIR = DATA_DIR / "editions"
HADITHS_DIR = DATA_DIR / "hadiths"
CHAPTERS_DIR = DATA_DIR / "chapters"

BASE_URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions"

EDITIONS = {
    "ara-bukhari": {
        "file": "ara-bukhari.min.json",
        "name": "Arabic (Vocalized with Tashkeel)",
        "language": "ar",
        "description": "Standard vocalized Arabic text of Sahih al-Bukhari with full tashkeel."
    },
    "ara-bukhari1": {
        "file": "ara-bukhari1.min.json",
        "name": "Arabic (Unvocalized Plain)",
        "language": "ar-plain",
        "description": "Normalized Arabic text without diacritics for fast fulltext search."
    },
    "eng-bukhari": {
        "file": "eng-bukhari.min.json",
        "name": "English (Dr. Muhammad Muhsin Khan)",
        "language": "en",
        "description": "Complete 9-volume translation by Dr. Muhammad Muhsin Khan."
    },
    "ind-bukhari": {
        "file": "ind-bukhari.min.json",
        "name": "Nusantara / Indonesian (Terjemahan Lengkap)",
        "language": "ms-id",
        "description": "Complete Nusantara translation of all hadiths."
    }
}

def fetch_json(url: str, retries: int = 3, delay: float = 2.0) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "MaktabahMaftoohah-BukhariBot/1.0"})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            if attempt == retries:
                raise
            print(f"  [Retry {attempt}/{retries}] Failed fetching {url}: {e}. Retrying...")
            time.sleep(delay * attempt)
    raise RuntimeError(f"Could not fetch {url}")

def run_etl():
    EDITIONS_DIR.mkdir(parents=True, exist_ok=True)
    HADITHS_DIR.mkdir(parents=True, exist_ok=True)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)

    loaded_editions = {}

    print("=== Step 1: Downloading & Archiving Fulltext Editions ===")
    for key, info in EDITIONS.items():
        out_path = EDITIONS_DIR / f"{key}.json"
        if out_path.exists():
            print(f"  Found cached edition: {out_path.name}")
            with open(out_path, "r", encoding="utf-8") as f:
                loaded_editions[key] = json.load(f)
        else:
            url = f"{BASE_URL}/{info['file']}"
            print(f"  Downloading {info['name']} from {url}...")
            data = fetch_json(url)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            loaded_editions[key] = data
            print(f"  Saved {len(data.get('hadiths', []))} hadiths to {out_path.name}")

    # Write editions manifest
    manifest = {
        "collection": "sahih-al-bukhari",
        "title": "Sahih al-Bukhari (صحيح البخاري)",
        "total_hadiths": len(loaded_editions["ara-bukhari"].get("hadiths", [])),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "editions": [
            {
                "id": k,
                "name": v["name"],
                "language": v["language"],
                "description": v["description"],
                "filename": f"{k}.json",
                "hadith_count": len(loaded_editions.get(k, {}).get("hadiths", []))
            }
            for k, v in EDITIONS.items()
        ]
    }
    with open(EDITIONS_DIR / "manifest.json", "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, ensure_ascii=False, indent=2)
    print("  Created data/editions/manifest.json")

    print("\n=== Step 2: Indexing and Mapping Hadiths by Book Number ===")
    ara_hadiths = loaded_editions["ara-bukhari"].get("hadiths", [])
    eng_hadiths = loaded_editions.get("eng-bukhari", {}).get("hadiths", [])
    ind_hadiths = loaded_editions.get("ind-bukhari", {}).get("hadiths", [])

    # Index by hadithnumber
    eng_map = {h["hadithnumber"]: h.get("text", "") for h in eng_hadiths}
    ind_map = {h["hadithnumber"]: h.get("text", "") for h in ind_hadiths}

    # Load existing books.json for canonical book titles
    books_file = DATA_DIR / "books.json"
    existing_books = []
    if books_file.exists():
        with open(books_file, "r", encoding="utf-8") as bf:
            existing_books = json.load(bf)
    books_dict = {b["book_number"]: b for b in existing_books}

    # Group Arabic hadiths by book number
    section_details = loaded_editions["ara-bukhari"].get("metadata", {}).get("section_details", {})
    sections = []
    for k, v in section_details.items():
        if k == '0' or not k.isdigit():
            continue
        try:
            sections.append((int(k), float(v['hadithnumber_first']), float(v['hadithnumber_last'])))
        except (ValueError, KeyError):
            pass
    sections.sort(key=lambda x: x[0])

    def resolve_book_id(h, last_known_book):
        ref_book = h.get("reference", {}).get("book")
        if ref_book and int(ref_book) > 0:
            return int(ref_book)
        hnum = float(h.get("hadithnumber", 0))
        for sec_id, first, last in sections:
            if first <= hnum <= last:
                return sec_id
        # Check gaps between sections
        for idx in range(len(sections) - 1):
            if sections[idx][2] < hnum < sections[idx + 1][1]:
                return sections[idx][0]
        return last_known_book or 1

    books_hadiths = {}
    current_book_tracker = 1
    for h in ara_hadiths:
        book_num = resolve_book_id(h, current_book_tracker)
        current_book_tracker = book_num
        if book_num not in books_hadiths:
            books_hadiths[book_num] = []
        books_hadiths[book_num].append(h)

    print(f"  Indexed {sum(len(v) for v in books_hadiths.values())} hadiths across {len(books_hadiths)} books.")

    print("\n=== Step 3: Generating Canonical Hadith Shards (01.json - 97.json) ===")
    updated_books = []

    for book_num in sorted(books_hadiths.keys()):
        h_list = books_hadiths[book_num]
        book_info = books_dict.get(book_num, {
            "book_number": book_num,
            "title_ms": f"Kitab {book_num}",
            "title_ar": f"كتاب {book_num}",
            "title_en": f"Book {book_num}"
        })

        shard_hadiths = []
        first_h_num = h_list[0]["hadithnumber"]
        last_h_num = h_list[-1]["hadithnumber"]

        for h in h_list:
            h_num = h["hadithnumber"]
            in_book = h.get("reference", {}).get("hadith")
            ar_text = h.get("text", "").strip()

            en_trans = eng_map.get(h_num, "").strip()
            ms_trans = ind_map.get(h_num, "").strip()

            # Normalize integer or float hadith number
            normalized_h_num = int(h_num) if float(h_num).is_integer() else float(h_num)

            canonical_h = {
                "collection_id": "sahih-al-bukhari",
                "hadith_number": normalized_h_num,
                "in_book_number": int(in_book) if in_book is not None and int(in_book) > 0 else None,
                "book_number": int(book_num),
                "book_title": {
                    "ar": book_info.get("title_ar", ""),
                    "ms": book_info.get("title_ms") or book_info.get("title", ""),
                    "en": book_info.get("title_en", "")
                },
                "arabic": ar_text,
                "gradings": [
                    {
                        "scholar": "Imam al-Bukhari",
                        "grade": "Sahih",
                        "grade_ar": "صحيح",
                        "notes": "Al-Jami' al-Sahih al-Musnad min Umur Rasulillah SAW wa Sunanihi wa Ayyamihi"
                    }
                ],
                "translations": {
                    "ms": ms_trans if ms_trans else en_trans,
                    "en": en_trans,
                    "id": ms_trans
                }
            }
            shard_hadiths.append(canonical_h)

        # Write shard file e.g. 01.json, 02.json, ..., 97.json
        shard_filename = f"{book_num:02d}.json"
        shard_path = HADITHS_DIR / shard_filename
        with open(shard_path, "w", encoding="utf-8") as sf:
            json.dump(shard_hadiths, sf, ensure_ascii=False, indent=2)

        # Build / update chapters for this book
        chapters_data = [
            {
                "chapter_number": 1,
                "title": book_info.get("title_ms") or book_info.get("title", ""),
                "title_ar": book_info.get("title_ar", ""),
                "hadith_range": f"{first_h_num}-{last_h_num}",
                "hadiths_count": len(shard_hadiths)
            }
        ]
        with open(CHAPTERS_DIR / shard_filename, "w", encoding="utf-8") as cf:
            json.dump(chapters_data, cf, ensure_ascii=False, indent=2)

        # Update book record
        book_info["hadith_range"] = f"{first_h_num}-{last_h_num}"
        book_info["hadiths_count"] = len(shard_hadiths)
        book_info["hadith_start"] = int(first_h_num)
        book_info["hadith_end"] = int(last_h_num)
        book_info["hadith_count"] = len(shard_hadiths)
        updated_books.append(book_info)

    # Save updated books.json
    with open(DATA_DIR / "books.json", "w", encoding="utf-8") as bf:
        json.dump(updated_books, bf, ensure_ascii=False, indent=2)

    # Update collection.json
    collection_path = DATA_DIR / "collection.json"
    collection_meta = {
        "collection": "sahih-al-bukhari",
        "title": "Maktabah Maftoohah — Sahih al-Bukhari",
        "title_ar": "صحيح البخاري",
        "total_books": len(updated_books),
        "total_hadiths": len(ara_hadiths),
        "seeded_books": [b["book_number"] for b in updated_books],
        "active_hadiths": len(ara_hadiths)
    }
    with open(collection_path, "w", encoding="utf-8") as colf:
        json.dump(collection_meta, colf, ensure_ascii=False, indent=2)

    print(f"  Successfully compiled {len(updated_books)} books into data/hadiths/ and data/chapters/!")
    print(f"  Total hadiths in collection: {len(ara_hadiths)}")
    return 0

if __name__ == "__main__":
    run_etl()
