/**
 * Maktabah Maftoohah Sahih al-Bukhari - Reader Application
 * Zero-Build ES6 Architecture
 */

import { analytics } from './analytics.js';

console.log('Maktabah Maftoohah Sahih al-Bukhari initialized.');

document.addEventListener('DOMContentLoaded', () => {
  analytics.init();

  const themeToggle = document.getElementById('themeToggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const isDark = document.body.getAttribute('data-theme') === 'dark';
      document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
      themeToggle.textContent = isDark ? '🌙' : '☀️';
    });
  }
});
