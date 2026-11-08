import json
from pathlib import Path

def test_project():
    root = Path(__file__).resolve().parent.parent
    assert (root / "index.html").exists(), "index.html missing"
    assert (root / "404.html").exists(), "404.html missing"
    assert (root / "assets" / "og-banner.jpg").exists(), "og-banner.jpg missing"
    assert (root / "assets" / "logo.svg").exists(), "logo.svg missing"
    assert (root / "assets" / "logo.png").exists(), "logo.png missing"
    assert (root / "assets" / "logo-mark.svg").exists(), "logo-mark.svg missing"
    assert (root / "assets" / "github-avatar.png").exists(), "github-avatar.png missing"
    assert (root / "assets" / "site-banner.png").exists(), "site-banner.png missing"
    assert (root / "1" / "index.html").exists(), "Hadith 1 OG page stub missing"
    assert (root / "AGENTS.md").exists(), "AGENTS.md missing"
    assert (root / ".nojekyll").exists(), ".nojekyll missing"
    assert (root / "data" / "books.json").exists(), "books.json missing"
    assert (root / "data" / "editions" / "manifest.json").exists(), "editions/manifest.json missing"
    assert (root / "data" / "scanned_editions.json").exists(), "scanned_editions.json missing"
    assert (root / "docs" / "SCANNED_EDITIONS.md").exists(), "SCANNED_EDITIONS.md missing"
    assert (root / "documents" / "sahih-al-bukhari.epub").exists(), "sahih-al-bukhari.epub missing"
    assert (root / "documents" / "bukhari-sultaniyyah-vol01.pdf").exists(), "bukhari-sultaniyyah-vol01.pdf missing"

    with open(root / "data" / "books.json", "r", encoding="utf-8") as f:
        books = json.load(f)
        assert len(books) == 97, f"Expected 97 books, found {len(books)}"

    print("Project structure & document verification PASSED for sahih-al-bukhari.")

if __name__ == "__main__":
    test_project()
