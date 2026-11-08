#!/usr/bin/env python3
"""
scripts/generate_branding.py
Generates official Maktabah Maftoohah branding assets for Sahih al-Bukhari:
- assets/og-banner.jpg (1200x630 Open Graph / Twitter Card Banner)
- assets/icon-192.png & assets/icon-512.png (PWA icons)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

def generate_banner():
    width, height = 1200, 630
    img = Image.new("RGB", (width, height), color="#064e3b")
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(height):
        ratio = y / height
        # interpolate from #064e3b (6, 78, 59) to #022c22 (2, 44, 34)
        r = int(6 * (1 - ratio) + 2 * ratio)
        g = int(78 * (1 - ratio) + 44 * ratio)
        b = int(59 * (1 - ratio) + 34 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Inner decorative border
    margin = 32
    draw.rounded_rectangle(
        [margin, margin, width - margin, height - margin],
        radius=20,
        outline="#10b981",
        width=2
    )
    draw.rounded_rectangle(
        [margin + 8, margin + 8, width - margin - 8, height - margin - 8],
        radius=14,
        outline="#047857",
        width=1
    )

    # Load system fonts
    try:
        font_brand = ImageFont.truetype("segoeuib.ttf", 28)
        font_title_ar = ImageFont.truetype("segoeui.ttf", 56)
        font_title = ImageFont.truetype("segoeuib.ttf", 64)
        font_sub = ImageFont.truetype("segoeui.ttf", 26)
        font_badge = ImageFont.truetype("segoeuib.ttf", 20)
    except Exception:
        font_brand = ImageFont.load_default()
        font_title_ar = font_brand
        font_title = font_brand
        font_sub = font_brand
        font_badge = font_brand

    # Header brand
    draw.text((80, 75), "MAKTABAH MAFTOOAH  |  المكتبة المفتوحة", font=font_brand, fill="#34d399")

    # Arabic title
    draw.text((80, 140), "الْجَامِعُ الْمُسْنَدُ الصَّحِيحُ — صَحِيحُ الْبُخَارِيِّ", font=font_title_ar, fill="#fbbf24")

    # Main Title
    draw.text((80, 230), "Sahih al-Bukhari", font=font_title, fill="#ffffff")

    # Subtitle
    draw.text(
        (80, 320),
        "Koleksi Hadis Autentik Lengkap (97 Kitab, 7,589 Hadis)",
        font=font_sub,
        fill="#cbd5e1"
    )
    draw.text(
        (80, 365),
        "Teks Arab Berbaris • Terjemahan Melayu & Inggeris • Sanad & Matn",
        font=font_sub,
        fill="#94a3b8"
    )

    # Feature badges
    badges = [
        "Zero-Build Vanilla ES6",
        "PWA Luar Talian (Offline)",
        "Naskhah Sultaniyyah (Bulaq 1311 H)",
        "Deep Link /1 - /7563"
    ]
    x_pos = 80
    y_pos = 460
    for b in badges:
        # Measure text box
        bbox = draw.textbbox((0, 0), b, font=font_badge)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.rounded_rectangle(
            [x_pos, y_pos, x_pos + tw + 28, y_pos + th + 16],
            radius=8,
            fill="#065f46",
            outline="#10b981",
            width=1
        )
        draw.text((x_pos + 14, y_pos + 6), b, font=font_badge, fill="#f8fafc")
        x_pos += tw + 44

    # Footer domain
    draw.text((80, 545), "maktabah-maftoohah.github.io/sahih-al-bukhari", font=font_brand, fill="#6ee7b7")

    out_file = ASSETS / "og-banner.jpg"
    img.save(out_file, "JPEG", quality=92, optimize=True)
    print(f"  Generated {out_file} ({out_file.stat().st_size} bytes)")

def generate_icons():
    for sz in (192, 512):
        img = Image.new("RGBA", (sz, sz), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Rounded rect emerald background
        draw.rounded_rectangle([0, 0, sz, sz], radius=int(sz * 0.18), fill="#047857")
        # Gold emblem in center
        margin = int(sz * 0.22)
        draw.rounded_rectangle(
            [margin, margin, sz - margin, sz - margin],
            radius=int(sz * 0.08),
            fill="#ffffff",
            outline="#d97706",
            width=max(2, int(sz * 0.015))
        )
        # Inner spine
        spine_w = int(sz * 0.08)
        draw.rectangle([margin, margin, margin + spine_w, sz - margin], fill="#065f46")
        out_file = ASSETS / f"icon-{sz}.png"
        img.save(out_file, "PNG")
        print(f"  Generated {out_file}")

if __name__ == "__main__":
    generate_banner()
    generate_icons()
