"""Seed Book 2 (Kitab al-Iman) for Sahih al-Bukhari with verified Hadith traditions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CHAPTERS_DIR = DATA_DIR / "chapters"
HADITHS_DIR = DATA_DIR / "hadiths"

CHAPTERS_BOOK_2 = [
  {"chapter_number": 1, "title_ar": "باب الإِيمَانُ وَقَوْلُ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «بُنِيَ الإِسْلاَمُ عَلَى خَمْسٍ»", "title_ms": "Bab: Iman dan Sabda Nabi ﷺ: 'Islam dibina atas lima perkara'", "title_en": "Chapter: Faith and the statement of the Prophet ﷺ: 'Islam is based on five'", "hadith_start": 8, "hadith_end": 8},
  {"chapter_number": 2, "title_ar": "باب أُمُورِ الإِيمَانِ وَقَوْلِ اللَّهِ تَعَالَى: {لَيْسَ الْبِرَّ أَنْ تُوَلُّوا وُجُوهَكُمْ}", "title_ms": "Bab: Perkara-perkara Iman", "title_en": "Chapter: Matters of Faith", "hadith_start": 9, "hadith_end": 9},
  {"chapter_number": 3, "title_ar": "باب الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ", "title_ms": "Bab: Seorang Muslim ialah yang orang Islam lain selamat dari lidah dan tangannya", "title_en": "Chapter: A Muslim is the one from whose tongue and hands Muslims are safe", "hadith_start": 10, "hadith_end": 11},
  {"chapter_number": 4, "title_ar": "باب أَيُّ الإِسْلاَمِ أَفْضَلُ؟", "title_ms": "Bab: Manakah amalan Islam yang paling afdhal?", "title_en": "Chapter: Which Islam is the best?", "hadith_start": 12, "hadith_end": 12},
  {"chapter_number": 5, "title_ar": "باب إِطْعَامُ الطَّعَامِ مِنَ الإِسْلاَمِ", "title_ms": "Bab: Memberi makan sebahagian daripada Islam", "title_en": "Chapter: To feed the people is a part of Islam", "hadith_start": 12, "hadith_end": 12},
  {"chapter_number": 6, "title_ar": "باب مِنَ الإِيمَانِ أَنْ يُحِبَّ لأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ", "title_ms": "Bab: Sebahagian daripada iman mengasihi saudaranya seperti mengasihi dirinya sendiri", "title_en": "Chapter: To love for one's brother what he loves for himself is part of faith", "hadith_start": 13, "hadith_end": 13},
  {"chapter_number": 7, "title_ar": "باب حُبُّ الرَّسُولِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ مِنَ الإِيمَانِ", "title_ms": "Bab: Mengasihi Rasulullah ﷺ adalah sebahagian daripada iman", "title_en": "Chapter: Loving the Messenger ﷺ is part of faith", "hadith_start": 14, "hadith_end": 15},
  {"chapter_number": 8, "title_ar": "باب حَلاَوَةِ الإِيمَانِ", "title_ms": "Bab: Manisnya Iman", "title_en": "Chapter: Sweetness of Faith", "hadith_start": 16, "hadith_end": 16},
  {"chapter_number": 9, "title_ar": "باب سُؤَالِ جِبْرِيلَ النَّبِيَّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ عَنِ الإِيمَانِ وَالإِسْلاَمِ وَالإِحْسَانِ", "title_ms": "Bab: Pertanyaan Jibril kepada Nabi ﷺ tentang Iman, Islam dan Ihsan", "title_en": "Chapter: Question of Gabriel about Iman, Islam and Ihsan", "hadith_start": 50, "hadith_end": 50}
]

HADITHS_BOOK_2 = [
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 8,
    "in_book_number": 1,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 1,
    "chapter_title": {"ar": "باب الإِيمَانُ وَقَوْلُ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «بُنِيَ الإِسْلاَمُ عَلَى خَمْسٍ»", "ms": "Bab: Iman dan Sabda Nabi ﷺ: 'Islam dibina atas lima perkara'", "en": "Chapter: Faith and the statement of the Prophet ﷺ: 'Islam is based on five'"},
    "arabic": "حَدَّثَنَا عُبَيْدُ اللَّهِ بْنُ مُوسَى، قَالَ: أَخْبَرَنَا حَنْظَلَةُ بْنُ أَبِي سُفْيَانَ، عَنْ عِكْرِمَةَ بْنِ خَالِدٍ، عَنِ ابْنِ عُمَرَ رَضِيَ اللَّهُ عَنْهُمَا قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: «بُنِيَ الإِسْلاَمُ عَلَى خَمْسٍ: شَهَادَةِ أَنْ لاَ إِلَهَ إِلاَّ اللَّهُ وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ، وَإِقَامِ الصَّلاَةِ، وَإِيتَاءِ الزَّكَاةِ، وَالْحَجِّ، وَصَوْمِ رَمَضَانَ».",
    "sanad_text": "حَدَّثَنَا عُبَيْدُ اللَّهِ بْنُ مُوسَى، قَالَ: أَخْبَرَنَا حَنْظَلَةُ بْنُ أَبِي سُفْيَانَ، عَنْ عِكْرِمَةَ بْنِ خَالِدٍ، عَنِ ابْنِ عُمَرَ رَضِيَ اللَّهُ عَنْهُمَا قَالَ: قَالَ رَسُولُ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "«بُنِيَ الإِسْلاَمُ عَلَى خَمْسٍ: شَهَادَةِ أَنْ لاَ إِلَهَ إِلاَّ اللَّهُ وَأَنَّ مُحَمَّدًا رَسُولُ اللَّهِ، وَإِقَامِ الصَّلاَةِ، وَإِيتَاءِ الزَّكَاةِ، وَالْحَجِّ، وَصَوْمِ رَمَضَانَ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Ibnu Umar r.a. katanya: Rasulullah ﷺ bersabda: 'Islam dibina di atas lima perkara: Penyaksian bahawa tiada tuhan melainkan Allah dan Muhammad adalah utusan Allah, mendirikan solat, menunaikan zakat, menunaikan haji, dan berpuasa pada bulan Ramadan.'",
      "en": "Narrated Ibn 'Umar: Allah's Messenger said: 'Islam is based on five principles: To testify that none has the right to be worshipped but Allah and Muhammad is Allah's Messenger, to establish the prayers, to pay Zakat, to perform Hajj, and to observe fast during the month of Ramadan.'"
    },
    "cross_references": [
      {"type": "quran", "surah": 3, "ayah": 97, "relation": "rukun_haji"}
    ],
    "tags": ["rukun-islam", "syahadah", "solat", "zakat", "puasa", "haji"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 9,
    "in_book_number": 2,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 2,
    "chapter_title": {"ar": "باب أُمُورِ الإِيمَانِ", "ms": "Bab: Perkara-perkara Iman", "en": "Chapter: Matters of Faith"},
    "arabic": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مُحَمَّدٍ، قَالَ: حَدَّثَنَا أَبُو عَامِرٍ الْعَقَدِيُّ، قَالَ: حَدَّثَنَا سُلَيْمَانُ بْنُ بِلاَلٍ، عَنْ عَبْدِ اللَّهِ بْنِ دِينَارٍ، عَنْ أَبِي صَالِحٍ، عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ: «الإِيمَانُ بِضْعٌ وَسِتُّونَ شُعْبَةً، وَالْحَيَاءُ شُعْبَةٌ مِنَ الإِيمَانِ».",
    "sanad_text": "حَدَّثَنَا عَبْدُ اللَّهِ بْنُ مُحَمَّدٍ، قَالَ: حَدَّثَنَا أَبُو عَامِرٍ الْعَقَدِيُّ، قَالَ: حَدَّثَنَا سُلَيْمَانُ بْنُ بِلاَلٍ، عَنْ عَبْدِ اللَّهِ بْنِ دِينَارٍ، عَنْ أَبِي صَالِحٍ، عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللَّهُ عَنْهُ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ:",
    "matn_text": "«الإِيمَانُ بِضْعٌ وَسِتُّونَ شُعْبَةً، وَالْحَيَاءُ شُعْبَةٌ مِنَ الإِيمَانِ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Abu Hurairah r.a., daripada Nabi ﷺ bersabda: 'Iman itu mempunyai enam puluh lebih cabang, dan sifat malu adalah salah satu cabang daripada iman.'",
      "en": "Narrated Abu Huraira: The Prophet said: 'Faith has over sixty branches, and Haya' (modesty/shyness) is a branch of faith.'"
    },
    "tags": ["cabang-iman", "malu", "akhlak"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 10,
    "in_book_number": 3,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 3,
    "chapter_title": {"ar": "باب الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ", "ms": "Bab: Seorang Muslim ialah yang orang Islam lain selamat dari lidah dan tangannya", "en": "Chapter: A Muslim is the one from whose tongue and hands Muslims are safe"},
    "arabic": "حَدَّثَنَا آدَمُ بْنُ أَبِي إِيَاسٍ، قَالَ: حَدَّثَنَا شُعْبَةُ، عَنْ عَبْدِ اللَّهِ بْنِ أَبِي السَّفَرِ، وَإِسْمَاعِيلَ، عَنِ الشَّعْبِيِّ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو رَضِيَ اللَّهُ عَنْهُمَا، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ: «الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ، وَالْمُهَاجِرُ مَنْ هَجَرَ مَا نَهَى اللَّهُ عَنْهُ».",
    "sanad_text": "حَدَّثَنَا آدَمُ بْنُ أَبِي إِيَاسٍ، قَالَ: حَدَّثَنَا شُعْبَةُ، عَنْ عَبْدِ اللَّهِ بْنِ أَبِي السَّفَرِ، وَإِسْمَاعِيلَ، عَنِ الشَّعْبِيِّ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو رَضِيَ اللَّهُ عَنْهُمَا، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ:",
    "matn_text": "«الْمُسْلِمُ مَنْ سَلِمَ الْمُسْلِمُونَ مِنْ لِسَانِهِ وَيَدِهِ، وَالْمُهَاجِرُ مَنْ هَجَرَ مَا نَهَى اللَّهُ عَنْهُ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Abdullah ibn 'Amr r.a., daripada Nabi ﷺ bersabda: 'Seorang Muslim (sejati) ialah sesiapa yang orang Islam lain selamat daripada kejahatan lidah dan tangannya, dan orang yang berhijrah ialah sesiapa yang meninggalkan apa yang dilarang oleh Allah.'",
      "en": "Narrated 'Abdullah bin 'Amr: The Prophet said: 'A Muslim is the one who avoids harming Muslims with his tongue and hands. And a Muhajir (emigrant) is the one who gives up all what Allah has forbidden.'"
    },
    "tags": ["definisi-muslim", "menjaga-lidah", "hijrah-maknawi"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 12,
    "in_book_number": 5,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 5,
    "chapter_title": {"ar": "باب إِطْعَامُ الطَّعَامِ مِنَ الإِسْلاَمِ", "ms": "Bab: Memberi makan sebahagian daripada Islam", "en": "Chapter: To feed the people is a part of Islam"},
    "arabic": "حَدَّثَنَا عَمْرُو بْنُ خَالِدٍ، قَالَ: حَدَّثَنَا اللَّيْثُ، عَنْ يَزِيدَ، عَنْ أَبِي الْخَيْرِ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو، أَنَّ رَجُلًا سَأَلَ النَّبِيَّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: أَيُّ الإِسْلاَمِ خَيْرٌ؟ قَالَ: «تُطْعِمُ الطَّعَامَ، وَتَقْرَأُ السَّلاَمَ عَلَى مَنْ عَرَفْتَ وَمَنْ لَمْ تَعْرِفْ».",
    "sanad_text": "حَدَّثَنَا عَمْرُو بْنُ خَالِدٍ، قَالَ: حَدَّثَنَا اللَّيْثُ، عَنْ يَزِيدَ، عَنْ أَبِي الْخَيْرِ، عَنْ عَبْدِ اللَّهِ بْنِ عَمْرٍو، أَنَّ رَجُلًا سَأَلَ النَّبِيَّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ:",
    "matn_text": "أَيُّ الإِسْلاَمِ خَيْرٌ؟ قَالَ: «تُطْعِمُ الطَّعَامَ، وَتَقْرَأُ السَّلاَمَ عَلَى مَنْ عَرَفْتَ وَمَنْ لَمْ تَعْرِفْ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Abdullah ibn 'Amr bahawa seorang lelaki bertanya kepada Nabi ﷺ: 'Amalan Islam manakah yang terbaik?' Baginda menjawab: 'Engkau memberi makan makanan, dan mengucapkan salam kepada orang yang engkau kenal dan orang yang tidak engkau kenal.'",
      "en": "Narrated 'Abdullah bin 'Amr: A man asked the Prophet: 'What sort of deeds in Islam are good?' The Prophet replied: 'To feed the people and greet those whom you know and those whom you do not know.'"
    },
    "tags": ["memberi-makan", "menebar-salam", "kebajikan"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 13,
    "in_book_number": 6,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 6,
    "chapter_title": {"ar": "باب مِنَ الإِيمَانِ أَنْ يُحِبَّ لأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ", "ms": "Bab: Sebahagian daripada iman mengasihi saudaranya seperti mengasihi dirinya sendiri", "en": "Chapter: To love for one's brother what he loves for himself is part of faith"},
    "arabic": "حَدَّثَنَا مُسَدَّدٌ، قَالَ: حَدَّثَنَا يَحْيَى، عَنْ شُعْبَةَ، عَنْ قَتَادَةَ، عَنْ أَنَسٍ رَضِيَ اللَّهُ عَنْهُ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ: «لاَ يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ».",
    "sanad_text": "حَدَّثَنَا مُسَدَّدٌ، قَالَ: حَدَّثَنَا يَحْيَى، عَنْ شُعْبَةَ، عَنْ قَتَادَةَ، عَنْ أَنَسٍ رَضِيَ اللَّهُ عَنْهُ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ:",
    "matn_text": "«لاَ يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Anas r.a., daripada Nabi ﷺ bersabda: 'Tidak sempurna iman seseorang daripada kamu sehinggalah dia mengasihi untuk saudaranya apa yang dia kasihi untuk dirinya sendiri.'",
      "en": "Narrated Anas: The Prophet said: 'None of you will have faith till he wishes for his (Muslim) brother what he likes for himself.'"
    },
    "tags": ["persaudaraan", "kasih-sayang", "kesempurnaan-iman"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 16,
    "in_book_number": 9,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 8,
    "chapter_title": {"ar": "باب حَلاَوَةِ الإِيمَانِ", "ms": "Bab: Manisnya Iman", "en": "Chapter: Sweetness of Faith"},
    "arabic": "حَدَّثَنَا مُحَمَّدُ بْنُ الْمُثَنَّى، قَالَ: حَدَّثَنَا عَبْدُ الْوَهَّابِ الثَّقَفِيُّ، قَالَ: حَدَّثَنَا أَيُّوبُ، عَنْ أَبِي قِلاَبَةَ، عَنْ أَنَسٍ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ: «ثَلاَثٌ مَنْ كُنَّ فِيهِ وَجَدَ حَلاَوَةَ الإِيمَانِ: أَنْ يَكُونَ اللَّهُ وَرَسُولُهُ أَحَبَّ إِلَيْهِ مِمَّا سِوَاهُمَا، وَأَنْ يُحِبَّ الْمَرْءَ لاَ يُحِبُّهُ إِلاَّ لِلَّهِ، وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ كَمَا يَكْرَهُ أَنْ يُقْذَفَ فِي النَّارِ».",
    "sanad_text": "حَدَّثَنَا مُحَمَّدُ بْنُ الْمُثَنَّى، قَالَ: حَدَّثَنَا عَبْدُ الْوَهَّابِ الثَّقَفِيُّ، قَالَ: حَدَّثَنَا أَيُّوبُ، عَنْ أَبِي قِلاَبَةَ، عَنْ أَنَسٍ، عَنِ النَّبِيِّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ قَالَ:",
    "matn_text": "«ثَلاَثٌ مَنْ كُنَّ فِيهِ وَجَدَ حَلاَوَةَ الإِيمَانِ: أَنْ يَكُونَ اللَّهُ وَرَسُولُهُ أَحَبَّ إِلَيْهِ مِمَّا سِوَاهُمَا، وَأَنْ يُحِبَّ الْمَرْءَ لاَ يُحِبُّهُ إِلاَّ لِلَّهِ، وَأَنْ يَكْرَهَ أَنْ يَعُودَ فِي الْكُفْرِ كَمَا يَكْرَهُ أَنْ يُقْذَفَ فِي النَّارِ».",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Daripada Anas r.a., daripada Nabi ﷺ bersabda: 'Tiga perkara yang sesiapa memilikinya akan merasai kemanisan iman: Hendaklah Allah dan Rasul-Nya lebih dicintai daripada selain keduanya, hendaklah dia mencintai seseorang semata-mata kerana Allah, dan hendaklah dia benci untuk kembali kepada kekufuran sebagaimana dia benci dicampakkan ke dalam api neraka.'",
      "en": "Narrated Anas: The Prophet said: 'Whoever possesses the following three qualities will taste the sweetness of faith: The one to whom Allah and His Messenger become dearer than anything else, who loves a person and he loves him only for Allah's sake, and who hates to revert to atheism (disbelief) as he hates to be thrown into the fire.'"
    },
    "tags": ["kemanisan-iman", "cinta-allah", "cinta-rasul", "ukhuwah"]
  },
  {
    "collection_id": "sahih-al-bukhari",
    "hadith_number": 50,
    "in_book_number": 43,
    "book_number": 2,
    "book_title": {"ar": "كتاب الإيمان", "ms": "Kitab Iman", "en": "Book of Belief"},
    "chapter_number": 9,
    "chapter_title": {"ar": "باب سُؤَالِ جِبْرِيلَ النَّبِيَّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ عَنِ الإِيمَانِ وَالإِسْلاَمِ وَالإِحْسَانِ", "ms": "Bab: Pertanyaan Jibril kepada Nabi ﷺ tentang Iman, Islam dan Ihsan", "en": "Chapter: Question of Gabriel about Iman, Islam and Ihsan"},
    "arabic": "حَدَّثَنَا مُسَدَّدٌ، قَالَ: حَدَّثَنَا إِسْمَاعِيلُ بْنُ إِبْرَاهِيمَ، أَخْبَرَنَا أَبُو حَيَّانَ التَّيْمِيُّ، عَنْ أَبِي زُرْعَةَ، عَنْ أَبِي هُرَيْرَةَ قَالَ: كَانَ النَّبِيُّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ بَارِزًا يَوْمًا لِلنَّاسِ، فَأَتَاهُ جِبْرِيلُ فَقَالَ: مَا الإِيمَانُ؟ قَالَ: «الإِيمَانُ أَنْ تُؤْمِنَ بِاللَّهِ وَمَلاَئِكَتِهِ، وَكُتُبِهِ، وَبِلِقَائِهِ، وَرُسُلِهِ، وَتُؤْمِنَ بِالْبَعْثِ». قَالَ: مَا الإِسْلاَمُ؟ قَالَ: «الإِسْلاَمُ أَنْ تَعْبُدَ اللَّهَ وَلاَ تُشْرِكَ بِهِ شَيْئًا، وَتُقِيمَ الصَّلاَةَ، وَتُؤَدِّيَ الزَّكَاةَ الْمَفْرُوضَةَ، وَتَصُومَ رَمَضَانَ». قَالَ: مَا الإِحْسَانُ؟ قَالَ: «أَنْ تَعْبُدَ اللَّهَ كَأَنَّكَ تَرَاهُ، فَإِنْ لَمْ تَكُنْ تَرَاهُ فَإِنَّهُ يَرَاكَ». قَالَ: مَتَى السَّاعَةُ؟ قَالَ: «مَا الْمَسْئُولُ عَنْهَا بِأَعْلَمَ مِنَ السَّائِلِ، وَسَأُخْبِرُكَ عَنْ أَشْرَاطِهَا: إِذَا وَلَدَتِ الأَمَةُ رَبَّتَهَا، وَإِذَا تَطَاوَلَ رُعَاةُ الإِبِلِ الْبُهْمُ فِي الْبُنْيَانِ، فِي خَمْسٍ لاَ يَعْلَمُهُنَّ إِلاَّ اللَّهُ». ثُمَّ تَلاَ النَّبِيُّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ: {إِنَّ اللَّهَ عِنْدَهُ عِلْمُ السَّاعَةِ} الآيَةَ. ثُمَّ أَدْبَرَ فَقَالَ: «رُدُّوهُ». فَلَمْ يَرَوْا شَيْئًا، فَقَالَ: «هَذَا جِبْرِيلُ جَاءَ يُعَلِّمُ النَّاسَ دِينَهُمْ».",
    "sanad_text": "حَدَّثَنَا مُسَدَّدٌ، قَالَ: حَدَّثَنَا إِسْمَاعِيلُ بْنُ إِبْرَاهِيمَ، أَخْبَرَنَا أَبُو حَيَّانَ التَّيْمِيُّ، عَنْ أَبِي زُرْعَةَ، عَنْ أَبِي هُرَيْرَةَ قَالَ:",
    "matn_text": "كَانَ النَّبِيُّ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ بَارِزًا يَوْمًا لِلنَّاسِ، فَأَتَاهُ جِبْرِيلُ فَقَالَ: مَا الإِيمَانُ؟ قَالَ: «الإِيمَانُ أَنْ تُؤْمِنَ بِاللَّهِ وَمَلاَئِكَتِهِ، وَكُتُبِهِ، وَبِلِقَائِهِ، وَرُسُلِهِ، وَتُؤْمِنَ بِالْبَعْثِ»...",
    "gradings": [{"scholar": "Imam al-Bukhari", "grade": "Sahih", "grade_ar": "صحيح"}],
    "translations": {
      "ms": "Hadis Jibril yang agung: Jibril a.s. datang dalam rupa seorang lelaki lalu bertanya kepada Rasulullah ﷺ tentang hakikat Iman, Islam, Ihsan ('Hendaklah engkau menyembah Allah seolah-olah engkau melihat-Nya, dan sekiranya engkau tidak melihat-Nya, sesungguhnya Dia melihatmu'), dan tanda-tanda Kiamat. Kemudian baginda bersabda: 'Ini adalah Jibril yang datang untuk mengajarkan manusia tentang agama mereka.'",
      "en": "The monumental Hadith of Gabriel: Gabriel came in the form of a man and questioned the Prophet ﷺ regarding the reality of Iman, Islam, Ihsan ('To worship Allah as if you see Him, and if you do not see Him, He sees you'), and the signs of the Hour. Then the Prophet said: 'That was Gabriel who came to teach the people their religion.'"
    },
    "cross_references": [
      {"type": "quran", "surah": 31, "ayah": 34, "relation": "quoted_ayah_in_hadith"}
    ],
    "tags": ["hadis-jibril", "iman", "islam", "ihsan", "tanda-kiamat", "teras-agama"]
  }
]

def main():
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    HADITHS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Write chapters/02.json
    chap_file = CHAPTERS_DIR / "02.json"
    with open(chap_file, "w", encoding="utf-8") as f:
        json.dump(CHAPTERS_BOOK_2, f, ensure_ascii=False, indent=2)
    print(f"Written {len(CHAPTERS_BOOK_2)} chapters to {chap_file}")

    # 2. Write hadiths/02.json
    hadith_file = HADITHS_DIR / "02.json"
    with open(hadith_file, "w", encoding="utf-8") as f:
        json.dump(HADITHS_BOOK_2, f, ensure_ascii=False, indent=2)
    print(f"Written {len(HADITHS_BOOK_2)} hadiths to {hadith_file}")

    # 3. Update collection.json
    coll_file = DATA_DIR / "collection.json"
    with open(coll_file, "r", encoding="utf-8") as f:
        coll_data = json.load(f)
    coll_data["seeded_books"] = [1, 2]
    coll_data["active_hadiths"] = coll_data.get("active_hadiths", 7) + len(HADITHS_BOOK_2)
    with open(coll_file, "w", encoding="utf-8") as f:
        json.dump(coll_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {coll_file}")

if __name__ == "__main__":
    main()
