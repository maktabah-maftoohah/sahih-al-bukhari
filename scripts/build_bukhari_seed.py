"""Seed script for Sahih al-Bukhari books and Book 1 data conforming to Maktabah Maftoohah standards."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
BOOKS_FILE = DATA_DIR / "books.json"
CHAPTERS_DIR = DATA_DIR / "chapters"
HADITHS_DIR = DATA_DIR / "hadiths"

# Canonical 97 books of Sahih al-Bukhari
BOOKS_DATA = [
  {"book_number": 1, "title_ar": "كتاب بدء الوحي", "title_ms": "Kitab Permulaan Wahyu", "title_en": "Book of Revelation", "hadith_start": 1, "hadith_end": 7, "hadith_count": 7},
  {"book_number": 2, "title_ar": "كتاب الإيمان", "title_ms": "Kitab Iman", "title_en": "Book of Belief (Faith)", "hadith_start": 8, "hadith_end": 58, "hadith_count": 51},
  {"book_number": 3, "title_ar": "كتاب العلم", "title_ms": "Kitab Ilmu", "title_en": "Book of Knowledge", "hadith_start": 59, "hadith_end": 134, "hadith_count": 76},
  {"book_number": 4, "title_ar": "كتاب الوضوء", "title_ms": "Kitab Wuduk", "title_en": "Book of Ablution (Wudu')", "hadith_start": 135, "hadith_end": 247, "hadith_count": 113},
  {"book_number": 5, "title_ar": "كتاب الغسل", "title_ms": "Kitab Mandi Wajib", "title_en": "Book of Bathing (Ghusl)", "hadith_start": 248, "hadith_end": 293, "hadith_count": 46},
  {"book_number": 6, "title_ar": "كتاب الحيض", "title_ms": "Kitab Haid", "title_en": "Book of Menstrual Periods", "hadith_start": 294, "hadith_end": 333, "hadith_count": 40},
  {"book_number": 7, "title_ar": "كتاب التيمم", "title_ms": "Kitab Tayamum", "title_en": "Book of Rubbing Hands and Face with Dust (Tayammum)", "hadith_start": 334, "hadith_end": 348, "hadith_count": 15},
  {"book_number": 8, "title_ar": "كتاب الصلاة", "title_ms": "Kitab Solat", "title_en": "Book of Prayers (Salat)", "hadith_start": 349, "hadith_end": 520, "hadith_count": 172},
  {"book_number": 9, "title_ar": "كتاب مواقيت الصلاة", "title_ms": "Kitab Waktu-Waktu Solat", "title_en": "Book of Times of the Prayers", "hadith_start": 521, "hadith_end": 602, "hadith_count": 82},
  {"book_number": 10, "title_ar": "كتاب الأذان", "title_ms": "Kitab Azan", "title_en": "Book of Call to Prayers (Adhan)", "hadith_start": 603, "hadith_end": 875, "hadith_count": 273},
  {"book_number": 11, "title_ar": "كتاب الجمعة", "title_ms": "Kitab Solat Jumaat", "title_en": "Book of Friday Prayer", "hadith_start": 876, "hadith_end": 941, "hadith_count": 66},
  {"book_number": 12, "title_ar": "كتاب صلاة الخوف", "title_ms": "Kitab Solat Khauf (Ketakutan)", "title_en": "Book of Fear Prayer", "hadith_start": 942, "hadith_end": 947, "hadith_count": 6},
  {"book_number": 13, "title_ar": "كتاب العيدين", "title_ms": "Kitab Dua Hari Raya", "title_en": "Book of The Two Festivals (Eids)", "hadith_start": 948, "hadith_end": 989, "hadith_count": 42},
  {"book_number": 14, "title_ar": "كتاب الوتر", "title_ms": "Kitab Solat Witir", "title_en": "Book of Witr Prayer", "hadith_start": 990, "hadith_end": 1004, "hadith_count": 15},
  {"book_number": 15, "title_ar": "كتاب الاستسقاء", "title_ms": "Kitab Solat Istisqa' (Minta Hujan)", "title_en": "Book of Invoking Allah for Rain (Istisqaa)", "hadith_start": 1005, "hadith_end": 1039, "hadith_count": 35},
  {"book_number": 16, "title_ar": "كتاب الكسوف", "title_ms": "Kitab Solat Gerhana (Khusuf)", "title_en": "Book of Eclipses", "hadith_start": 1040, "hadith_end": 1066, "hadith_count": 27},
  {"book_number": 17, "title_ar": "كتاب سجود القرآن", "title_ms": "Kitab Sujud Tilawah", "title_en": "Book of Prostration During Quran Recitation", "hadith_start": 1067, "hadith_end": 1079, "hadith_count": 13},
  {"book_number": 18, "title_ar": "كتاب تقصير الصلاة", "title_ms": "Kitab Memendekkan Solat (Qasar)", "title_en": "Book of Shortening the Prayers", "hadith_start": 1080, "hadith_end": 1119, "hadith_count": 40},
  {"book_number": 19, "title_ar": "كتاب التهجد", "title_ms": "Kitab Solat Tahajud", "title_en": "Book of Prayer at Night (Tahajjud)", "hadith_start": 1120, "hadith_end": 1187, "hadith_count": 68},
  {"book_number": 20, "title_ar": "كتاب فضل الصلاة في مسجد مكة والمدينة", "title_ms": "Kitab Keutamaan Solat di Masjid Makkah & Madinah", "title_en": "Book of Virtues of Prayer in Makkah & Madinah", "hadith_start": 1188, "hadith_end": 1197, "hadith_count": 10},
  {"book_number": 21, "title_ar": "كتاب العمل في الصلاة", "title_ms": "Kitab Perbuatan Dalam Solat", "title_en": "Book of Actions while Praying", "hadith_start": 1198, "hadith_end": 1223, "hadith_count": 26},
  {"book_number": 22, "title_ar": "كتاب السهو", "title_ms": "Kitab Sujud Sahwi", "title_en": "Book of Forgetfulness in Prayer", "hadith_start": 1224, "hadith_end": 1236, "hadith_count": 13},
  {"book_number": 23, "title_ar": "كتاب الجنائز", "title_ms": "Kitab Jenazah", "title_en": "Book of Funerals (Al-Jana'iz)", "hadith_start": 1237, "hadith_end": 1394, "hadith_count": 158},
  {"book_number": 24, "title_ar": "كتاب الزكاة", "title_ms": "Kitab Zakat", "title_en": "Book of Zakat", "hadith_start": 1395, "hadith_end": 1512, "hadith_count": 118},
  {"book_number": 25, "title_ar": "كتاب الحج", "title_ms": "Kitab Haji", "title_en": "Book of Hajj (Pilgrimage)", "hadith_start": 1513, "hadith_end": 1772, "hadith_count": 260},
  {"book_number": 26, "title_ar": "كتاب العمرة", "title_ms": "Kitab Umrah", "title_en": "Book of Umrah (Minor Pilgrimage)", "hadith_start": 1773, "hadith_end": 1805, "hadith_count": 33},
  {"book_number": 27, "title_ar": "كتاب المحصر", "title_ms": "Kitab Halangan Ihram (Muhsar)", "title_en": "Book of Pilgrims Prevented from Completing Hajj", "hadith_start": 1806, "hadith_end": 1820, "hadith_count": 15},
  {"book_number": 28, "title_ar": "كتاب جزاء الصيد", "title_ms": "Kitab Denda Memburu Ketika Berihram", "title_en": "Book of Penalty for Hunting While in Ihram", "hadith_start": 1821, "hadith_end": 1866, "hadith_count": 46},
  {"book_number": 29, "title_ar": "كتاب فضائل المدينة", "title_ms": "Kitab Keutamaan Kota Madinah", "title_en": "Book of Virtues of Madinah", "hadith_start": 1867, "hadith_end": 1903, "hadith_count": 37},
  {"book_number": 30, "title_ar": "كتاب الصوم", "title_ms": "Kitab Puasa", "title_en": "Book of Fasting (Sawm)", "hadith_start": 1904, "hadith_end": 2007, "hadith_count": 104},
  {"book_number": 31, "title_ar": "كتاب صلاة التراويح", "title_ms": "Kitab Solat Tarawih", "title_en": "Book of Tarawih Prayers", "hadith_start": 2008, "hadith_end": 2013, "hadith_count": 6},
  {"book_number": 32, "title_ar": "كتاب فضل ليلة القدر", "title_ms": "Kitab Keutamaan Lailatul Qadar", "title_en": "Book of Virtues of Night of Qadr", "hadith_start": 2014, "hadith_end": 2024, "hadith_count": 11},
  {"book_number": 33, "title_ar": "كتاب الاعتكاف", "title_ms": "Kitab Iktikaf", "title_en": "Book of Retiring to a Mosque (I'tikaf)", "hadith_start": 2025, "hadith_end": 2046, "hadith_count": 22},
  {"book_number": 34, "title_ar": "كتاب البيوع", "title_ms": "Kitab Jual Beli", "title_en": "Book of Sales and Trade", "hadith_start": 2047, "hadith_end": 2238, "hadith_count": 192},
  {"book_number": 35, "title_ar": "كتاب السلم", "title_ms": "Kitab Bai' Salam (Jual Beli Tempahan)", "title_en": "Book of As-Salam (Forward Buying)", "hadith_start": 2239, "hadith_end": 2256, "hadith_count": 18},
  {"book_number": 36, "title_ar": "كتاب الشفعة", "title_ms": "Kitab Hak Syuf'ah", "title_en": "Book of Pre-emption (Shuf'a)", "hadith_start": 2257, "hadith_end": 2259, "hadith_count": 3},
  {"book_number": 37, "title_ar": "كتاب الإجارة", "title_ms": "Kitab Sewa-Menyewa (Ijarah)", "title_en": "Book of Hiring (Ijarah)", "hadith_start": 2260, "hadith_end": 2286, "hadith_count": 27},
  {"book_number": 38, "title_ar": "كتاب الحوالة", "title_ms": "Kitab Pemindahan Hutang (Hawalah)", "title_en": "Book of Transfer of Debt (Hawalah)", "hadith_start": 2287, "hadith_end": 2289, "hadith_count": 3},
  {"book_number": 39, "title_ar": "كتاب الكفالة", "title_ms": "Kitab Jaminan (Kafalah)", "title_en": "Book of Suretyship (Kafalah)", "hadith_start": 2290, "hadith_end": 2298, "hadith_count": 9},
  {"book_number": 40, "title_ar": "كتاب الوكالة", "title_ms": "Kitab Perwakilan (Wakalah)", "title_en": "Book of Representation (Agency)", "hadith_start": 2299, "hadith_end": 2319, "hadith_count": 21},
  {"book_number": 41, "title_ar": "كتاب المزارعة", "title_ms": "Kitab Pertanian dan Muzara'ah", "title_en": "Book of Agriculture and Cultivation", "hadith_start": 2320, "hadith_end": 2350, "hadith_count": 31},
  {"book_number": 42, "title_ar": "كتاب المساقاة", "title_ms": "Kitab Pengairan (Musaqat)", "title_en": "Book of Distribution of Water", "hadith_start": 2351, "hadith_end": 2384, "hadith_count": 34},
  {"book_number": 43, "title_ar": "كتاب الاستقراض", "title_ms": "Kitab Pinjaman dan Pembayaran Hutang", "title_en": "Book of Loans, Debts and Bankruptcy", "hadith_start": 2385, "hadith_end": 2409, "hadith_count": 25},
  {"book_number": 44, "title_ar": "كتاب الخصومات", "title_ms": "Kitab Pertikaian (Khusumat)", "title_en": "Book of Disputes and Quarrels", "hadith_start": 2410, "hadith_end": 2425, "hadith_count": 16},
  {"book_number": 45, "title_ar": "كتاب اللقطة", "title_ms": "Kitab Barang Temuan (Luqathah)", "title_en": "Book of Lost Property Found by Others", "hadith_start": 2426, "hadith_end": 2439, "hadith_count": 14},
  {"book_number": 46, "title_ar": "كتاب المظالم", "title_ms": "Kitab Kezaliman dan Hak yang Dirampas", "title_en": "Book of Oppressions (Mazalim)", "hadith_start": 2440, "hadith_end": 2482, "hadith_count": 43},
  {"book_number": 47, "title_ar": "كتاب الشركة", "title_ms": "Kitab Perkongsian (Syirkah)", "title_en": "Book of Partnership", "hadith_start": 2483, "hadith_end": 2507, "hadith_count": 25},
  {"book_number": 48, "title_ar": "كتاب الرهن", "title_ms": "Kitab Gadaian (Rahn)", "title_en": "Book of Mortgaging", "hadith_start": 2508, "hadith_end": 2516, "hadith_count": 9},
  {"book_number": 49, "title_ar": "كتاب العتق", "title_ms": "Kitab Memerdekakan Hamba ('Itq)", "title_en": "Book of Manumission of Slaves", "hadith_start": 2517, "hadith_end": 2559, "hadith_count": 43},
  {"book_number": 50, "title_ar": "كتاب المكاتب", "title_ms": "Kitab Perjanjian Kemerdekaan Hamba (Mukatab)", "title_en": "Book of Mukatab (Emancipation Contract)", "hadith_start": 2560, "hadith_end": 2565, "hadith_count": 6},
  {"book_number": 51, "title_ar": "كتاب الهبة وفضلها", "title_ms": "Kitab Hadiah dan Keutamaannya (Hibah)", "title_en": "Book of Gifts (Hibah)", "hadith_start": 2566, "hadith_end": 2636, "hadith_count": 71},
  {"book_number": 52, "title_ar": "كتاب الشهادات", "title_ms": "Kitab Penyaksian (Syahadat)", "title_en": "Book of Witnesses (Shahadat)", "hadith_start": 2637, "hadith_end": 2689, "hadith_count": 53},
  {"book_number": 53, "title_ar": "كتاب الصلح", "title_ms": "Kitab Perdamaian (Sulh)", "title_en": "Book of Peacemaking (Reconciliation)", "hadith_start": 2690, "hadith_end": 2710, "hadith_count": 21},
  {"book_number": 54, "title_ar": "كتاب الشروط", "title_ms": "Kitab Syarat-Syarat", "title_en": "Book of Conditions", "hadith_start": 2711, "hadith_end": 2737, "hadith_count": 27},
  {"book_number": 55, "title_ar": "كتاب الوصايا", "title_ms": "Kitab Wasiat", "title_en": "Book of Wills and Testaments (Wasiyyah)", "hadith_start": 2738, "hadith_end": 2781, "hadith_count": 44},
  {"book_number": 56, "title_ar": "كتاب الجهاد والسير", "title_ms": "Kitab Jihad dan Ekspedisi", "title_en": "Book of Fighting for the Cause of Allah (Jihad)", "hadith_start": 2782, "hadith_end": 3090, "hadith_count": 309},
  {"book_number": 57, "title_ar": "كتاب فرض الخمس", "title_ms": "Kitab Kewajipan Seperlima Harta Rampasan (Khums)", "title_en": "Book of One-Fifth of Booty to the Cause of Allah", "hadith_start": 3091, "hadith_end": 3155, "hadith_count": 65},
  {"book_number": 58, "title_ar": "كتاب الجزية والموادعة", "title_ms": "Kitab Jizyah dan Perjanjian Damai", "title_en": "Book of Jizyah and Tax", "hadith_start": 3156, "hadith_end": 3189, "hadith_count": 34},
  {"book_number": 59, "title_ar": "كتاب بدء الخلق", "title_ms": "Kitab Permulaan Makhluk", "title_en": "Book of Beginning of Creation", "hadith_start": 3190, "hadith_end": 3325, "hadith_count": 136},
  {"book_number": 60, "title_ar": "كتاب أحاديث الأنبياء", "title_ms": "Kitab Kisah Para Nabi", "title_en": "Book of Stories of the Prophets", "hadith_start": 3326, "hadith_end": 3488, "hadith_count": 163},
  {"book_number": 61, "title_ar": "كتاب المناقب", "title_ms": "Kitab Keutamaan dan Sifat Sahabat (Manaqib)", "title_en": "Book of Virtues and Merits of the Prophet and Companions", "hadith_start": 3489, "hadith_end": 3648, "hadith_count": 160},
  {"book_number": 62, "title_ar": "كتاب فضائل أصحاب النبي", "title_ms": "Kitab Keutamaan Para Sahabat Nabi ﷺ", "title_en": "Book of Companions of the Prophet", "hadith_start": 3649, "hadith_end": 3775, "hadith_count": 127},
  {"book_number": 63, "title_ar": "كتاب مناقب الأنصار", "title_ms": "Kitab Keutamaan Kaum Ansar", "title_en": "Book of Merits of the Ansar", "hadith_start": 3776, "hadith_end": 3948, "hadith_count": 173},
  {"book_number": 64, "title_ar": "كتاب المغازي", "title_ms": "Kitab Peperangan Nabi ﷺ (Maghazi)", "title_en": "Book of Military Expeditions led by the Prophet (Al-Maghazi)", "hadith_start": 3949, "hadith_end": 4473, "hadith_count": 525},
  {"book_number": 65, "title_ar": "كتاب التفسير", "title_ms": "Kitab Tafsir al-Quran", "title_en": "Book of Prophetic Commentary on the Quran (Tafseer)", "hadith_start": 4474, "hadith_end": 4977, "hadith_count": 504},
  {"book_number": 66, "title_ar": "كتاب فضائل القرآن", "title_ms": "Kitab Keutamaan al-Quran", "title_en": "Book of Virtues of the Quran", "hadith_start": 4978, "hadith_end": 5062, "hadith_count": 85},
  {"book_number": 67, "title_ar": "كتاب النكاح", "title_ms": "Kitab Nikah (Perkahwinan)", "title_en": "Book of Wedlock, Marriage (Nikah)", "hadith_start": 5063, "hadith_end": 5250, "hadith_count": 188},
  {"book_number": 68, "title_ar": "كتاب الطلاق", "title_ms": "Kitab Talak (Perceraian)", "title_en": "Book of Divorce", "hadith_start": 5251, "hadith_end": 5350, "hadith_count": 100},
  {"book_number": 69, "title_ar": "كتاب النفقات", "title_ms": "Kitab Nafkah", "title_en": "Book of Supporting the Family", "hadith_start": 5351, "hadith_end": 5372, "hadith_count": 22},
  {"book_number": 70, "title_ar": "كتاب الأطعمة", "title_ms": "Kitab Makanan", "title_en": "Book of Foods and Meals", "hadith_start": 5373, "hadith_end": 5466, "hadith_count": 94},
  {"book_number": 71, "title_ar": "كتاب العقيقة", "title_ms": "Kitab Aqiqah", "title_en": "Book of Sacrifice for Newborn (Aqiqa)", "hadith_start": 5467, "hadith_end": 5474, "hadith_count": 8},
  {"book_number": 72, "title_ar": "كتاب الذبائح والصيد", "title_ms": "Kitab Sembelihan dan Buruan", "title_en": "Book of Slaughtering and Hunting", "hadith_start": 5475, "hadith_end": 5544, "hadith_count": 70},
  {"book_number": 73, "title_ar": "كتاب الأضاحي", "title_ms": "Kitab Korban (Udhiyyah)", "title_en": "Book of Al-Adha Festival Sacrifice", "hadith_start": 5545, "hadith_end": 5574, "hadith_count": 30},
  {"book_number": 74, "title_ar": "كتاب الأشربة", "title_ms": "Kitab Minuman", "title_en": "Book of Drinks", "hadith_start": 5575, "hadith_end": 5639, "hadith_count": 65},
  {"book_number": 75, "title_ar": "كتاب المرضى", "title_ms": "Kitab Orang Sakit", "title_en": "Book of Patients and Disease", "hadith_start": 5640, "hadith_end": 5677, "hadith_count": 38},
  {"book_number": 76, "title_ar": "كتاب الطب", "title_ms": "Kitab Perubatan (At-Tibb)", "title_en": "Book of Medicine", "hadith_start": 5678, "hadith_end": 5782, "hadith_count": 105},
  {"book_number": 77, "title_ar": "كتاب اللباس", "title_ms": "Kitab Pakaian", "title_en": "Book of Dress", "hadith_start": 5783, "hadith_end": 5969, "hadith_count": 187},
  {"book_number": 78, "title_ar": "كتاب الأدب", "title_ms": "Kitab Adab dan Akhlak", "title_en": "Book of Good Manners and Form (Al-Adab)", "hadith_start": 5970, "hadith_end": 6226, "hadith_count": 257},
  {"book_number": 79, "title_ar": "كتاب الاستئذان", "title_ms": "Kitab Meminta Izin (Isti'zan)", "title_en": "Book of Asking Permission", "hadith_start": 6227, "hadith_end": 6303, "hadith_count": 77},
  {"book_number": 80, "title_ar": "كتاب الدعوات", "title_ms": "Kitab Doa-Doa", "title_en": "Book of Invocations (Supplications)", "hadith_start": 6304, "hadith_end": 6411, "hadith_count": 108},
  {"book_number": 81, "title_ar": "كتاب الرقاق", "title_ms": "Kitab Kelembutan Hati (Riqaq)", "title_en": "Book of Heart-Melting Traditions (Ar-Riqaq)", "hadith_start": 6412, "hadith_end": 6593, "hadith_count": 182},
  {"book_number": 82, "title_ar": "كتاب القدر", "title_ms": "Kitab Qadar (Ketetapan Ilahi)", "title_en": "Book of Divine Will (Al-Qadar)", "hadith_start": 6594, "hadith_end": 6620, "hadith_count": 27},
  {"book_number": 83, "title_ar": "كتاب الأيمان والنذور", "title_ms": "Kitab Sumpah dan Nazar", "title_en": "Book of Oaths and Vows", "hadith_start": 6621, "hadith_end": 6707, "hadith_count": 87},
  {"book_number": 84, "title_ar": "كتاب كفارات الأيمان", "title_ms": "Kitab Kifarah Sumpah", "title_en": "Book of Expiation for Unfulfilled Oaths", "hadith_start": 6708, "hadith_end": 6722, "hadith_count": 15},
  {"book_number": 85, "title_ar": "كتاب الفرائض", "title_ms": "Kitab Pembahagian Pusaka (Faraid)", "title_en": "Book of Laws of Inheritance (Al-Fara'id)", "hadith_start": 6723, "hadith_end": 6771, "hadith_count": 49},
  {"book_number": 86, "title_ar": "كتاب الحدود", "title_ms": "Kitab Hukuman Hudud", "title_en": "Book of Limits and Punishments (Hudud)", "hadith_start": 6772, "hadith_end": 6860, "hadith_count": 89},
  {"book_number": 87, "title_ar": "كتاب الديات", "title_ms": "Kitab Diyat (Ganti Rugi Jenayah)", "title_en": "Book of Blood Money (Ad-Diyat)", "hadith_start": 6861, "hadith_end": 6917, "hadith_count": 57},
  {"book_number": 88, "title_ar": "كتاب استتابة المرتدين والمعاندين", "title_ms": "Kitab Meminta Taubat Orang Murtad", "title_en": "Book of Apostates and Rebels", "hadith_start": 6918, "hadith_end": 6939, "hadith_count": 22},
  {"book_number": 89, "title_ar": "كتاب الإكراه", "title_ms": "Kitab Paksaan (Ikrah)", "title_en": "Book of Coercion", "hadith_start": 6940, "hadith_end": 6952, "hadith_count": 13},
  {"book_number": 90, "title_ar": "كتاب الحيل", "title_ms": "Kitab Helah Hukum (Hiyal)", "title_en": "Book of Legal Tricks (Hiyal)", "hadith_start": 6953, "hadith_end": 6981, "hadith_count": 29},
  {"book_number": 91, "title_ar": "كتاب التعبير", "title_ms": "Kitab Tafsir Mimpi (Ta'bir)", "title_en": "Book of Interpretation of Dreams", "hadith_start": 6982, "hadith_end": 7047, "hadith_count": 66},
  {"book_number": 92, "title_ar": "كتاب الفتن", "title_ms": "Kitab Fitnah-Fitnah Akhir Zaman", "title_en": "Book of Afflictions and End of the World", "hadith_start": 7048, "hadith_end": 7136, "hadith_count": 89},
  {"book_number": 93, "title_ar": "كتاب الأحكام", "title_ms": "Kitab Kehakiman dan Pemerintahan (Ahkam)", "title_en": "Book of Judgments and Rulings", "hadith_start": 7137, "hadith_end": 7225, "hadith_count": 89},
  {"book_number": 94, "title_ar": "كتاب التمني", "title_ms": "Kitab Cita-Cita dan Harapan (Tamanni)", "title_en": "Book of Wishes", "hadith_start": 7226, "hadith_end": 7245, "hadith_count": 20},
  {"book_number": 95, "title_ar": "كتاب أخبار الآحاد", "title_ms": "Kitab Berita Ahad (Khabar al-Wahid)", "title_en": "Book of Holding on to Single-Narrator Reports", "hadith_start": 7246, "hadith_end": 7267, "hadith_count": 22},
  {"book_number": 96, "title_ar": "كتاب الاعتصام بالكتاب والسنة", "title_ms": "Kitab Berpegang Teguh Kepada al-Quran dan Sunnah", "title_en": "Book of Holding Fast to the Quran and Sunnah", "hadith_start": 7268, "hadith_end": 7370, "hadith_count": 103},
  {"book_number": 97, "title_ar": "كتاب التوحيد", "title_ms": "Kitab Tauhid", "title_en": "Book of Islamic Monotheism (Tawhid)", "hadith_start": 7371, "hadith_end": 7563, "hadith_count": 193}
]

# Book 1 Chapters
CHAPTERS_BOOK_1 = [
  {"chapter_number": 1, "title_ar": "باب كَيْفَ كَانَ بَدْءُ الْوَحْيِ إِلَى رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ", "title_ms": "Bab: Bagaimana permulaan wahyu diturunkan kepada Rasulullah ﷺ", "title_en": "Chapter: How the Divine Inspiration started to Allah's Messenger ﷺ", "hadith_start": 1, "hadith_end": 1},
  {"chapter_number": 2, "title_ar": "باب", "title_ms": "Bab", "title_en": "Chapter", "hadith_start": 2, "hadith_end": 2},
  {"chapter_number": 3, "title_ar": "باب", "title_ms": "Bab", "title_en": "Chapter", "hadith_start": 3, "hadith_end": 3},
  {"chapter_number": 4, "title_ar": "باب", "title_ms": "Bab", "title_en": "Chapter", "hadith_start": 4, "hadith_end": 4},
  {"chapter_number": 5, "title_ar": "باب", "title_ms": "Bab", "title_en": "Chapter", "hadith_start": 5, "hadith_end": 5},
  {"chapter_number": 6, "title_ar": "باب", "title_ms": "Bab", "title_en": "Chapter", "hadith_start": 6, "hadith_end": 7}
]

# Book 1 Hadiths 1-7
HADITHS_BOOK_1 = [
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 1,
    "in_book_number": 1,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب كَيْفَ كَانَ بَدْءُ الْوَحْيِ إِلَى رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ", "ms": "Bab: Bagaimana permulaan wahyu diturunkan kepada Rasulullah ﷺ", "en": "Chapter: How the Divine Inspiration started to Allah's Messenger ﷺ"},
    "arabic": "حَدَّثَنَا الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ، قَالَ: حَدَّثَنَا سُفْيَانُ، قَالَ: حَدَّثَنَا يَحْيَى بْنُ سَعِيدٍ الأَنْصَارِيُّ، قَالَ: أَخْبَرَنِي مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ، أَنَّهُ سَمِعَ عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ، يَقُولُ: سَمِعْتُ عُمَرَ بْنَ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ قَالَ: سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَقُولُ: «إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ».",
    "sanad_text": "حَدَّثَنَا الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ، قَالَ: حَدَّثَنَا سُفْيَانُ، قَالَ: حَدَّثَنَا يَحْيَى بْنُ سَعِيدٍ الأَنْصَارِيُّ، قَالَ: أَخْبَرَنِي مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ، أَنَّهُ سَمِعَ عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ، يَقُولُ: سَمِعْتُ عُمَرَ بْنَ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ قَالَ: سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَقُولُ:",
    "matn_text": "«إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Sesungguhnya setiap amalan itu bergantung kepada niat, dan sesungguhnya bagi setiap orang apa yang dia niatkan. Maka barangsiapa yang hijrahnya kerana dunia yang ingin diperolehinya atau kerana wanita yang ingin dinikahinya, maka hijrahnya itu adalah kepada apa yang dia berhijrah kepadanya.",
      "en": "Actions are but by intentions, and every man shall have but that which he intended. Thus he whose migration was for Allah and His Messenger, his migration was for Allah and His Messenger, and he whose migration was for worldly benefit or for a woman to marry, his migration was for what he migrated to."
    },
    "cross_references": [
      {"type": "quran", "surah": 4, "ayah": 163, "relation": "bab_ayah_evidence"}
    ],
    "tags": ["niat", "keikhlasan", "hijrah", "asas-islam"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 2,
    "in_book_number": 2,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 2,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ يُوسُفَ، قَالَ: أَخْبَرَنَا مَالِكٌ، عَنْ هِشَامِ بْنِ عُرْوَةَ، عَنْ أَبِيهِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ رَضِيَ اللَّهُ عَنْهَا، أَنَّ الْحَارِثَ بْنَ هِشَامٍ رَضِيَ اللَّهُ عَنْهُ سَأَلَ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ فَقَالَ: يَا رَسُولَ اللَّهِ، كَيْفَ يَأْتِيكَ الْوَحْيُ؟ فَقَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «أَحْيَانًا يَأْتِينِي مِثْلَ صَلْصَلَةِ الْجَرَسِ، وَهُوَ أَشَدُّهُ عَلَيَّ، فَيُفْصَمُ عَنِّي وَقَدْ وَعَيْتُ عَنْهُ مَا قَالَ، وَأَحْيَانًا يَتَمَثَّلُ لِيَ الْمَلَكُ رَجُلًا فَيُكَلِّمُنِي فَأَعِي مَا يَقُولُ». قَالَتْ عَائِشَةُ رَضِيَ اللَّهُ عَنْهَا: وَلَقَدْ رَأَيْتُهُ يَنْزِلُ عَلَيْهِ الْوَحْيُ فِي الْيَوْمِ الشَّدِيدِ الْبَرْدِ، فَيَفْصِمُ عَنْهُ وَإِنَّ جَبِينَهُ لَيَتَفَصَّدُ عَرَقًا.",
    "sanad_text": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ يُوسُفَ، قَالَ: أَخْبَرَنَا مَالِكٌ، عَنْ هِشَامِ بْنِ عُرْوَةَ، عَنْ أَبِيهِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ رَضِيَ اللَّهُ عَنْهَا، أَنَّ الْحَارِثَ بْنَ هِشَامٍ رَضِيَ اللَّهُ عَنْهُ سَأَلَ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ فَقَالَ:",
    "matn_text": "يَا رَسُولَ اللَّهِ، كَيْفَ يَأْتِيكَ الْوَحْيُ؟ فَقَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «أَحْيَانًا يَأْتِينِي مِثْلَ صَلْصَلَةِ الْجَرَسِ، وَهُوَ أَشَدُّهُ عَلَيَّ، فَيُفْصَمُ عَنِّي وَقَدْ وَعَيْتُ عَنْهُ مَا قَالَ، وَأَحْيَانًا يَتَمَثَّلُ لِيَ الْمَلَكُ رَجُلًا فَيُكَلِّمُنِي فَأَعِي مَا يَقُولُ». قَالَتْ عَائِشَةُ رَضِيَ اللَّهُ عَنْهَا: وَلَقَدْ رَأَيْتُهُ يَنْزِلُ عَلَيْهِ الْوَحْيُ فِي الْيَوْمِ الشَّدِيدِ الْبَرْدِ، فَيَفْصِمُ عَنْهُ وَإِنَّ جَبِينَهُ لَيَتَفَصَّدُ عَرَقًا.",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Al-Harith ibn Hisham bertanya: 'Wahai Rasulullah, bagaimanakah wahyu datang kepadamu?' Rasulullah ﷺ menjawab: 'Kadang-kadang ia datang kepadaku seperti gemerincing loceng, dan itulah keadaan yang paling berat bagiku, lalu ia terputus dariku dan aku telah memahami apa yang disampaikannya. Dan kadang-kadang malaikat menjelma kepadaku sebagai seorang lelaki lalu berbicara denganku dan aku memahami apa yang dia katakan.' 'Aisyah r.a. berkata: 'Sesungguhnya aku pernah melihat baginda diturunkan wahyu pada hari yang sangat dingin, lalu wahyu itu terhenti sementara dahi baginda mengalirkan peluh.'",
      "en": "Al-Harith bin Hisham asked Allah's Messenger: 'O Allah's Messenger! How is the Divine Inspiration revealed to you?' Allah's Messenger replied: 'Sometimes it is revealed like the ringing of a bell, this form of Inspiration is the hardest of all and then this state passes off after I have grasped what is inspired. Sometimes the Angel comes in the form of a man and talks to me and I grasp whatever he says.' 'A'ishah added: Verily I saw the Prophet being inspired Divinely on a very cold day and noticed the sweat dropping from his forehead."
    },
    "tags": ["sifat-wahyu", "malaikat", "kenabian"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 3,
    "in_book_number": 3,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 3,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا يَحْيَى بْنُ بُكَيْرٍ، قَالَ: حَدَّثَنَا اللَّيْثُ، عَنْ عُقَيْلٍ، عَنِ ابْنِ شِهَابٍ، عَنْ عُرْوَةَ بْنِ الزُّبَيْرِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ أَنَّهَا قَالَتْ: أَوَّلُ مَا بُدِئَ بِهِ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مِنَ الْوَحْيِ الرُّؤْيَا الصَّالِحَةُ فِي النَّوْمِ، فَكَانَ لاَ يَرَى رُؤْيَا إِلاَّ جَاءَتْ مِثْلَ فَلَقِ الصُّبْحِ، ثُمَّ حُبِّبَ إِلَيْهِ الْخَلاَءُ، وَكَانَ يَخْلُو بِغَارِ حِرَاءٍ فَيَتَحَنَّثُ فِيهِ - وَهُوَ التَّعَبُّدُ - اللَّيَالِيَ ذَوَاتِ الْعَدَدِ قَبْلَ أَنْ يَنْزِعَ إِلَى أَهْلِهِ، وَيَتَزَوَّدُ لِذَلِكَ، ثُمَّ يَرْجِعُ إِلَى خَدِيجَةَ فَيَتَزَوَّدُ لِمِثْلِهَا، حَتَّى جَاءَهُ الْحَقُّ وَهُوَ فِي غَارِ حِرَاءٍ، فَجَاءَهُ الْمَلَكُ فَقَالَ: اقْرَأْ. قُلْتُ: «مَا أَنَا بِقَارِئٍ». قَالَ: «فَأَخَذَنِي فَغَطَّنِي حَتَّى بَلَغَ مِنِّي الْجَهْدَ ثُمَّ أَرْسَلَنِي»، فَقَالَ: اقْرَأْ. قُلْتُ: «مَا أَنَا بِقَارِئٍ». فَأَخَذَنِي فَغَطَّنِي الثَّانِيَةَ حَتَّى بَلَغَ مِنِّي الْجَهْدَ ثُمَّ أَرْسَلَنِي، فَقَالَ: اقْرَأْ. فَقُلْتُ: «مَا أَنَا بِقَارِئٍ». فَأَخَذَنِي فَغَطَّنِي الثَّالِثَةَ ثُمَّ أَرْسَلَنِي، فَقَالَ: {اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ * خَلَقَ الإِنْسَانَ مِنْ عَلَقٍ * اقْرَأْ وَرَبُّكَ الأَكْرَمُ}، فَرَجَعَ بِهَا رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَرْجُفُ فُؤَادُهُ، فَدَخَلَ عَلَى خَدِيجَةَ بِنْتِ خُوَيْلِدٍ رَضِيَ اللَّهُ عَنْهَا، فَقَالَ: «زَمِّلُونِي زَمِّلُونِي». فَزَمَّلُوهُ حَتَّى ذَهَبَ عَنْهُ الرَّوْعُ...",
    "sanad_text": "حَدَّثَنَا يَحْيَى بْنُ بُكَيْرٍ، قَالَ: حَدَّثَنَا اللَّيْثُ، عَنْ عُقَيْلٍ، عَنِ ابْنِ شِهَابٍ، عَنْ عُرْوَةَ بْنِ الزُّبَيْرِ، عَنْ عَائِشَةَ أُمِّ الْمُؤْمِنِينَ أَنَّهَا قَالَتْ:",
    "matn_text": "أَوَّلُ مَا بُدِئَ بِهِ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مِنَ الْوَحْيِ الرُّؤْيَا الصَّالِحَةُ فِي النَّوْمِ، فَكَانَ لاَ يَرَى رُؤْيَا إِلاَّ جَاءَتْ مِثْلَ فَلَقِ الصُّبْحِ، ثُمَّ حُبِّبَ إِلَيْهِ الْخَلاَءُ، وَكَانَ يَخْلُو بِغَارِ حِرَاءٍ فَيَتَحَنَّثُ فِيهِ... فَرَجَعَ بِهَا رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَرْجُفُ فُؤَادُهُ...",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "'Aisyah r.a. meriwayatkan: Permulaan wahyu kepada Rasulullah ﷺ bermula dengan mimpi yang benar ketika tidur. Tidaklah baginda melihat mimpi melainkan ia datang nyata seperti terangnya fajar pagi. Kemudian baginda suka menyendiri di Gua Hira' untuk beribadah beberapa malam sebelum pulang kepada keluarganya... sehinggalah datang kepada baginda kebenaran ketika di Gua Hira', lalu malaikat datang dan berkata: 'Bacalah!' Baginda menjawab: 'Aku tidak pandai membaca'... lalu malaikat memegang dan merangkul baginda sehingga baginda merasa sesak, kemudian melepaskannya sambil membaca: {Bacalah dengan nama Tuhanmu yang menciptakan...}",
      "en": "'A'ishah narrated: The commencement of the Divine Inspiration to Allah's Messenger was in the form of good dreams which came true like bright day light, and then the love of seclusion was bestowed upon him. He used to go in seclusion in the cave of Hira where he used to worship continuously for many days... till suddenly the Truth descended upon him while he was in the cave of Hira. The Angel came to him and asked him to read. The Prophet replied, 'I do not know how to read.' The Prophet added, 'The Angel caught me and pressed me so hard that I could not bear it any more... then released me and said: Read in the Name of your Lord who created...'"
    },
    "cross_references": [
      {"type": "quran", "surah": 96, "ayah": 1, "relation": "first_revealed_verses"}
    ],
    "tags": ["gua-hira", "jibril", "iqra", "khadijah", "waraqah"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 4,
    "in_book_number": 4,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 4,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا مُوسَى بْنُ إِسْمَاعِيلَ، قَالَ: حَدَّثَنَا أَبُو عَوَانَةَ، قَالَ: حَدَّثَنَا مُوسَى بْنُ أَبِي عَائِشَةَ، قَالَ: حَدَّثَنَا سَعِيدُ بْنُ جُبَيْرٍ، عَنِ ابْنِ عَبَّاسٍ فِي قَوْلِهِ تَعَالَى: {لاَ تُحَرِّكْ بِهِ لِسَانَكَ لِتَعْجَلَ بِهِ} [القيامة: 16] قَالَ: كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يُعَالِجُ مِنَ التَّنْزِيلِ شِدَّةً، وَكَانَ مِمَّا يُحَرِّكُ شَفَتَيْهِ - فَقَالَ ابْنُ عَبَّاسٍ: فَأَنَا أُحَرِّكُهُمَا لَكُمْ كَمَا كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يُحَرِّكُهُمَا، وَقَالَ سَعِيدٌ: أَنَا أُحَرِّكُهُمَا كَمَا رَأَيْتُ ابْنَ عَبَّاسٍ يُحَرِّكُهُمَا، فَحَرَّكَ شَفَتَيْهِ - فَأَنْزَلَ اللَّهُ تَعَالَى: {لاَ تُحَرِّكْ بِهِ لِسَانَكَ لِتَعْجَلَ بِهِ * إِنَّ عَلَيْنَا جَمْعَهُ وَقُرْآنَهُ} قَالَ: جَمْعُهُ لَكَ فِي صَدْرِكَ وَتَقْرَأَهُ: {فَإِذَا قَرَأْنَاهُ فَاتَّبِعْ قُرْآنَهُ} قَالَ: فَاسْتَمِعْ لَهُ وَأَنْصِتْ: {ثُمَّ إِنَّ عَلَيْنَا بَيَانَهُ} ثُمَّ إِنَّ عَلَيْنَا أَنْ تَقْرَأَهُ، فَكَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ بَعْدَ ذَلِكَ إِذَا أَتَاهُ جِبْرِيلُ اسْتَمَعَ، فَإِذَا انْطَلَقَ جِبْرِيلُ قَرَأَهُ النَّبِيُّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ كَمَا قَرَأَهُ.",
    "sanad_text": "حَدَّثَنَا مُوسَى بْنُ إِسْمَاعِيلَ، قَالَ: حَدَّثَنَا أَبُو عَوَانَةَ، قَالَ: حَدَّثَنَا مُوسَى بْنُ أَبِي عَائِشَةَ، قَالَ: حَدَّثَنَا سَعِيدُ بْنُ جُبَيْرٍ، عَنِ ابْنِ عَبَّاسٍ فِي قَوْلِهِ تَعَالَى:",
    "matn_text": "{لاَ تُحَرِّكْ بِهِ لِسَانَكَ لِتَعْجَلَ بِهِ} قَالَ: كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يُعَالِجُ مِنَ التَّنْزِيلِ شِدَّةً، وَكَانَ مِمَّا يُحَرِّكُ شَفَتَيْهِ...",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Ibnu Abbas meriwayatkan mengenai firman Allah: {Janganlah engkau gerakkan lidahmu untuk membacanya kerana hendak cepat menghafalnya}: Rasulullah ﷺ menanggung keberatan ketika menerima wahyu dan baginda sering menggerakkan kedua-dua bibirnya dengan cepat... Maka Allah menurunkan ayat: {Sesungguhnya atas tanggungan Kamilah mengumpulkannya di dalam dadamu dan membacakannya...}",
      "en": "Ibn Abbas narrated regarding the verse: 'Do not move your tongue concerning (the Quran) to make haste therewith': Allah's Messenger used to bear the revelation with great effort and used to move his lips quickly. Allah revealed: 'It is for Us to collect it and to give you the ability to recite it...'"
    },
    "cross_references": [
      {"type": "quran", "surah": 75, "ayah": 16, "relation": "tafsir_ayat"}
    ],
    "tags": ["quran", "penurunan-wahyu", "surah-al-qiyamah"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 5,
    "in_book_number": 5,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 5,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا عَبْدَانُ، قَالَ: أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ: أَخْبَرَنَا يُونُسُ، عَنِ الزُّهْرِيِّ، ح وَحَدَّثَنَا بِشْرُ بْنُ مُحَمَّدٍ، قَالَ: أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ: أَخْبَرَنَا يُونُسُ، وَمَعْمَرٌ، عَنِ الزُّهْرِيِّ بِهَذَا الإِسْنَادِ، قَالَ: أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ، عَنِ ابْنِ عَبَّاسٍ، قَالَ: «كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ أَجْوَدَ النَّاسِ، وَكَانَ أَجْوَدُ مَا يَكُونُ فِي رَمَضَانَ حِينَ يَلْقَاهُ جِبْرِيلُ، وَكَانَ يَلْقَاهُ فِي كُلِّ لَيْلَةٍ مِنْ رَمَضَانَ فَيُدَارِسُهُ الْقُرْآنَ، فَلَرَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ أَجْوَدُ بِالْخَيْرِ مِنَ الرِّيحِ الْمُرْسَلَةِ».",
    "sanad_text": "حَدَّثَنَا عَبْدَانُ، قَالَ: أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ: أَخْبَرَنَا يُونُسُ، عَنِ الزُّهْرِيِّ، ح وَحَدَّثَنَا بِشْرُ بْنُ مُحَمَّدٍ، قَالَ: أَخْبَرَنَا عَبْدُ اللَّهِ، قَالَ: أَخْبَرَنَا يُونُسُ، وَمَعْمَرٌ، عَنِ الزُّهْرِيِّ بِهَذَا الإِسْنَادِ، قَالَ: أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ، عَنِ ابْنِ عَبَّاسٍ، قَالَ:",
    "matn_text": "«كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ أَجْوَدَ النَّاسِ، وَكَانَ أَجْوَدُ مَا يَكُونُ فِي رَمَضَانَ حِينَ يَلْقَاهُ جِبْرِيلُ، وَكَانَ يَلْقَاهُ فِي كُلِّ لَيْلَةٍ مِنْ رَمَضَانَ فَيُدَارِسُهُ الْقُرْآنَ، فَلَرَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ أَجْوَدُ بِالْخَيْرِ مِنَ الرِّيحِ الْمُرْسَلَةِ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Ibnu Abbas meriwayatkan: Rasulullah ﷺ adalah manusia yang paling pemurah, dan baginda paling pemurah pada bulan Ramadan ketika bertemu dengan Jibril. Jibril menemuinya pada setiap malam di bulan Ramadan untuk bertadarus al-Quran bersama baginda. Maka sesungguhnya Rasulullah ﷺ lebih pemurah dalam melakukan kebaikan daripada angin yang bertiup kencang.",
      "en": "Ibn Abbas narrated: Allah's Messenger was the most generous of all the people, and he used to reach the peak in generosity in the month of Ramadan when Gabriel met him. Gabriel used to meet him every night of Ramadan to rehearse the Quran with him. Verily, Allah's Messenger was more generous with goodness than the blowing wind."
    },
    "tags": ["ramadan", "kedermawanan", "jibril", "tadarus-quran"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 6,
    "in_book_number": 6,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 6,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مَحَمَّدٍ النُّفَيْلِيُّ، قَالَ: حَدَّثَنَا عُثْمَانُ بْنُ عُمَرَ، قَالَ: أَخْبَرَنَا يُونُسُ، عَنِ الزُّهْرِيِّ، قَالَ: حَدَّثَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ، أَنَّ ابْنَ عَبَّاسٍ، أَخْبَرَهُ: أَنَّ أَبَا سُفْيَانَ بْنَ حَرْبٍ أَخْبَرَهُ: أَنَّ هِرَقْلَ أَرْسَلَ إِلَيْهِ فِي رَكْبٍ مِنْ قُرَيْشٍ، وَكَانُوا تِجَارًا بِالشَّأْمِ فِي الْمُدَّةِ الَّتِي كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مَادَّ فِيهَا أَبَا سُفْيَانَ وَكُفَّارَ قُرَيْشٍ...",
    "sanad_text": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مَحَمَّدٍ النُّفَيْلِيُّ، قَالَ: حَدَّثَنَا عُثْمَانُ بْنُ عُمَرَ، قَالَ: أَخْبَرَنَا يُونُسُ، عَنِ الزُّهْرِيِّ، قَالَ: حَدَّثَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ، أَنَّ ابْنَ عَبَّاسٍ، أَخْبَرَهُ: أَنَّ أَبَا سُفْيَانَ بْنَ حَرْبٍ أَخْبَرَهُ:",
    "matn_text": "أَنَّ هِرَقْلَ أَرْسَلَ إِلَيْهِ فِي رَكْبٍ مِنْ قُرَيْشٍ، وَكَانُوا تِجَارًا بِالشَّأْمِ فِي الْمُدَّةِ الَّتِي كَانَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مَادَّ فِيهَا أَبَا سُفْيَانَ وَكُفَّارَ قُرَيْشٍ...",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Ibnu Abbas meriwayatkan bahawa Abu Sufyan ibn Harb memberitahunya: Heraklius (Maharaja Rom) telah menghantar utusan memanggilnya bersama sekumpulan kafilah Quraisy ketika mereka sedang berniaga di Syam dalam tempoh gencatan senjata antara Rasulullah ﷺ dan kaum kafir Quraisy...",
      "en": "Ibn Abbas narrated that Abu Sufyan bin Harb informed him that Heraclius had sent a messenger to him while he had been accompanying a caravan from Quraysh who were merchants doing business in Sham, during the truce between Allah's Messenger and the Quraysh..."
    },
    "tags": ["heraklius", "abu-sufyan", "surat-dakwah", "syam"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 7,
    "in_book_number": 7,
    "book_number": 1,
    "book_title": {"ar": "كتاب بدء الوحي", "ms": "Kitab Permulaan Wahyu", "en": "Book of Revelation"},
    "chapter_number": 6,
    "chapter_title": {"ar": "باب", "ms": "Bab", "en": "Chapter"},
    "arabic": "حَدَّثَنَا أَبُو الْيَمَانِ الْحَكَمُ بْنُ نَافِعٍ، قَالَ: أَخْبَرَنَا شُعَيْبٌ، عَنِ الزُّهْرِيِّ، قَالَ: أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ بْنِ عُتْبَةَ بْنِ مَسْعُودٍ، أَنَّ عَبْدَ اللَّهِ بْنَ عَبَّاسٍ أَخْبَرَهُ: أَنَّ أَبَا سُفْيَانَ بْنَ حَرْبٍ أَخْبَرَهُ: أَنَّ هِرَقْلَ أَرْسَلَ إِلَيْهِ فِي رَكْبٍ مِنْ قُرَيْشٍ... فَأَرْسَلَ هِرَقْلُ إِلَى أُسْقُفٍّ لَهُ ضَجَاطِرَ يُعَادِلُهُ فِي الْعِلْمِ، فَكَتَبَ إِلَيْهِ يُثْبِتُ مَبْعَثَ مُحَمَّدٍ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، وَأَنَّهُ هُوَ النَّبِيُّ الَّذِي نَنْتَظِرُهُ...",
    "sanad_text": "حَدَّثَنَا أَبُو الْيَمَانِ الْحَكَمُ بْنُ نَافِعٍ، قَالَ: أَخْبَرَنَا شُعَيْبٌ، عَنِ الزُّهْرِيِّ، قَالَ: أَخْبَرَنِي عُبَيْدُ اللَّهِ بْنُ عَبْدِ اللَّهِ بْنِ عُتْبَةَ بْنِ مَسْعُودٍ، أَنَّ عَبْدَ اللَّهِ بْنَ عَبَّاسٍ أَخْبَرَهُ: أَنَّ أَبَا سُفْيَانَ بْنَ حَرْبٍ أَخْبَرَهُ:",
    "matn_text": "أَنَّ هِرَقْلَ أَرْسَلَ إِلَيْهِ فِي رَكْبٍ مِنْ قُرَيْشٍ... كِتَابُ رَسُولِ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ، مِنْ مُحَمَّدٍ عَبْدِ اللَّهِ وَرَسُولِهِ إِلَى هِرَقْلَ عَظِيمِ الرُّومِ، سَلاَمٌ عَلَى مَنِ اتَّبَعَ الْهُدَى، أَمَّا بَعْدُ، فَإِنِّي أَدْعُوكَ بِدِعَايَةِ الإِسْلاَمِ، أَسْلِمْ تَسْلَمْ، يُؤْتِكَ اللَّهُ أَجْرَكَ مَرَّتَيْنِ...»",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Hadith lengkap dialog bersejarah antara Heraklius dan Abu Sufyan tentang peribadi Rasulullah ﷺ, kejujuran baginda, pengikutnya yang semakin bertambah, seruan kepada tauhid, dan surat baginda kepada Heraklius: 'Dengan nama Allah Yang Maha Pemurah lagi Maha Penyayang. Daripada Muhammad hamba Allah dan Rasul-Nya kepada Heraklius pembesar Rom. Kesejahteraan ke atas sesiapa yang mengikut petunjuk... Masuklah Islam nescaya kamu selamat...'",
      "en": "The comprehensive dialogue of Heraclius and Abu Sufyan investigating the Prophet's background, character, integrity, lineage, and message, and the Prophet's famous missive: 'In the name of Allah, the Most Gracious, the Most Merciful. From Muhammad, the slave of Allah and His Apostle to Heraclius the ruler of Byzantine: Peace be upon him who follows the right path... Embrace Islam and you will be safe...'"
    },
    "cross_references": [
      {"type": "quran", "surah": 3, "ayah": 64, "relation": "quoted_in_prophetic_letter"}
    ],
    "tags": ["heraklius", "dakwah-antarabangsa", "surat-nabi", "sifat-kenabian"]
  }
]

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    HADITHS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Write books.json
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(BOOKS_DATA, f, ensure_ascii=False, indent=2)
    print(f"Written {len(BOOKS_DATA)} books to {BOOKS_FILE}")

    # 2. Write chapters/01.json
    chap_file = CHAPTERS_DIR / "01.json"
    with open(chap_file, "w", encoding="utf-8") as f:
        json.dump(CHAPTERS_BOOK_1, f, ensure_ascii=False, indent=2)
    print(f"Written {len(CHAPTERS_BOOK_1)} chapters to {chap_file}")

    # 3. Write hadiths/01.json
    hadith_file = HADITHS_DIR / "01.json"
    with open(hadith_file, "w", encoding="utf-8") as f:
        json.dump(HADITHS_BOOK_1, f, ensure_ascii=False, indent=2)
    print(f"Written {len(HADITHS_BOOK_1)} hadiths to {hadith_file}")

    # 4. Update collection.json
    coll_file = DATA_DIR / "collection.json"
    coll_data = {
      "collection": "sahih-al-bukhari",
      "title": "Maktabah Maftoohah — Sahih al-Bukhari",
      "title_ar": "صحيح البخاري",
      "total_books": 97,
      "total_hadiths": 7563,
      "seeded_books": [1],
      "active_hadiths": len(HADITHS_BOOK_1)
    }
    with open(coll_file, "w", encoding="utf-8") as f:
        json.dump(coll_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {coll_file}")

if __name__ == "__main__":
    main()
