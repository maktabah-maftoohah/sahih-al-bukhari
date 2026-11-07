/**
 * Maktabah Maftoohah Sahih al-Bukhari - Reader Application
 * Zero-Build Vanilla ES6 Architecture
 */

import { analytics } from './analytics.js';

class BukhariReader {
  constructor() {
    this.currentLang = 'ms'; // Default Nusantara Malay
    this.currentBook = 1;
    this.books = [];
    this.hadiths = [];

    this.contentView = document.getElementById('contentView');
    this.langToggle = document.getElementById('langToggle');
    this.themeToggle = document.getElementById('themeToggle');
  }

  async init() {
    analytics.init();
    this.setupEventListeners();
    await this.loadBooks();
    await this.loadHadiths(this.currentBook);
  }

  setupEventListeners() {
    if (this.themeToggle) {
      this.themeToggle.addEventListener('click', () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
        this.themeToggle.textContent = isDark ? '🌙' : '☀️';
      });
    }

    if (this.langToggle) {
      this.langToggle.addEventListener('click', () => {
        this.currentLang = this.currentLang === 'ms' ? 'en' : 'ms';
        this.langToggle.textContent = this.currentLang === 'ms' ? 'MY' : 'EN';
        this.render();
      });
    }
  }

  async loadBooks() {
    try {
      const res = await fetch('./data/books.json');
      if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
      this.books = await res.json();
    } catch (e) {
      console.error('Failed to load books catalogue:', e);
      this.books = [];
    }
  }

  async loadHadiths(bookNumber) {
    this.contentView.innerHTML = '<p class="loading-state">Memuatkan hadis...</p>';
    const padded = String(bookNumber).padStart(2, '0');
    try {
      const res = await fetch(`./data/hadiths/${padded}.json`);
      if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
      this.hadiths = await res.json();
      this.render();
    } catch (e) {
      console.warn(`Book ${bookNumber} not yet seeded:`, e);
      this.hadiths = [];
      this.renderUnseeded(bookNumber);
    }
  }

  renderUnseeded(bookNumber) {
    const book = this.books.find(b => b.book_number === bookNumber) || {};
    const title = this.currentLang === 'ms' ? (book.title_ms || book.title_ar) : (book.title_en || book.title_ar);
    this.contentView.innerHTML = `
      <div class="hadith-card" style="text-align: center; padding: 3rem 1rem;">
        <h3 style="margin-bottom: 0.5rem;">${title} (${book.title_ar || ''})</h3>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          ${this.currentLang === 'ms' 
            ? 'Kitab ini dalam proses penyusunan dan pengesahan teks autentik.' 
            : 'This book is scheduled for text verification and ingestion.'}
        </p>
        <button class="btn-pill" id="backToBook1">
          ${this.currentLang === 'ms' ? 'Kembali ke Kitab 1 (Permulaan Wahyu)' : 'Return to Book 1 (Revelation)'}
        </button>
      </div>
    `;
    const btn = document.getElementById('backToBook1');
    if (btn) {
      btn.addEventListener('click', () => {
        this.currentBook = 1;
        const selector = document.getElementById('bookSelector');
        if (selector) selector.value = '1';
        this.loadHadiths(1);
      });
    }
  }

  render() {
    const currentBookObj = this.books.find(b => b.book_number === this.currentBook) || {};
    const bookTitle = this.currentLang === 'ms' 
      ? (currentBookObj.title_ms || currentBookObj.title_ar) 
      : (currentBookObj.title_en || currentBookObj.title_ar);

    // Book Selector Header
    const selectorHtml = `
      <div class="hero-section">
        <div class="book-control-row">
          <label for="bookSelector" style="font-weight: 600;">
            ${this.currentLang === 'ms' ? 'Pilih Kitab:' : 'Select Book:'}
          </label>
          <select id="bookSelector" class="book-select">
            ${this.books.map(b => {
              const bName = this.currentLang === 'ms' ? b.title_ms : b.title_en;
              return `<option value="${b.book_number}" ${b.book_number === this.currentBook ? 'selected' : ''}>
                ${b.book_number}. ${bName} (${b.title_ar})
              </option>`;
            }).join('')}
          </select>
          <div class="book-meta">
            <span class="badge">${this.hadiths.length} ${this.currentLang === 'ms' ? 'Hadis Aktif' : 'Active Hadiths'}</span>
            <span class="badge badge-sahih">Sahih al-Bukhari</span>
          </div>
        </div>
      </div>
    `;

    // Hadith Cards List
    const hadithListHtml = `
      <div class="hadith-list">
        ${this.hadiths.map(h => this.renderHadithCard(h)).join('')}
      </div>
    `;

    this.contentView.innerHTML = selectorHtml + hadithListHtml;

    // Attach selector change handler
    const selector = document.getElementById('bookSelector');
    if (selector) {
      selector.addEventListener('change', (e) => {
        this.currentBook = parseInt(e.target.value, 10);
        this.loadHadiths(this.currentBook);
      });
    }
  }

  renderHadithCard(hadith) {
    const trans = hadith.translations?.[this.currentLang] || hadith.translations?.ms || '';
    const grade = hadith.gradings?.[0]?.grade || 'Sahih';
    const gradeAr = hadith.gradings?.[0]?.grade_ar || 'صحيح';

    const crossRefsHtml = (hadith.cross_references || []).map(cr => {
      if (cr.type === 'quran') {
        return `<span class="badge badge-crossref">Surah ${cr.surah}:${cr.ayah}</span>`;
      }
      return '';
    }).join('');

    return `
      <article class="hadith-card" id="hadith-${hadith.hadith_number}">
        <div class="hadith-meta-bar">
          <div class="hadith-num-group">
            <span class="badge" style="background: var(--primary); color: #fff;">
              # ${hadith.hadith_number}
            </span>
            <span class="badge">
              ${this.currentLang === 'ms' ? 'Kitab' : 'Book'} ${hadith.book_number} : ${hadith.in_book_number}
            </span>
          </div>
          <div>
            <span class="badge badge-sahih">${gradeAr} / ${grade}</span>
          </div>
        </div>

        <div class="hadith-arabic">
          ${hadith.sanad_text ? `<span class="arabic-sanad">${hadith.sanad_text} </span>` : ''}
          <span class="arabic-matn">${hadith.matn_text || hadith.arabic}</span>
        </div>

        <div class="hadith-translation">
          ${trans}
        </div>

        <div class="hadith-footer">
          <div class="cross-ref-list">
            ${crossRefsHtml}
          </div>
          <div>
            ${hadith.tags ? hadith.tags.map(t => `<span style="margin-left: 0.25rem;">#${t}</span>`).join(' ') : ''}
          </div>
        </div>
      </article>
    `;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const reader = new BukhariReader();
  reader.init();
});
