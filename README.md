# 🕵️‍♂️ HeXacamu OSINT Tool

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/github/stars/yourusername/hexacamu?style=social" alt="GitHub stars">
</p>

> Ein vielseitiges OSINT-Tool zum Extrahieren von öffentlichen Informationen aus Instagram, YouTube und X (ehemals Twitter). Ideal für Recherchezwecke und Analyse öffentlicher Inhalte.

---

## 🧠 Features

- 🔍 **Instagram**:
  - Extrahiert Bilder aus Profilen über eine GraphQL-Abfrage
  - Erstellt eine automatisch generierte HTML-Galerie
  - Holt Profilbilder direkt aus dem Instagram-Quellcode

- 📺 **YouTube**:
  - Extrahiert alle Video-URLs aus einem Channel oder einer Playlist
  - Speichert sie sauber in einer `.txt`-Datei

- 🐦 **Twitter/X**:
  - Holt Medien (Bilder/Videos) von Benutzerprofilen via Bearer Token (API v2)
  - Speichert alle gefundenen URLs in einem Zeitstempel-basierten Log

---

## 🚀 Installation

```bash
pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet tweepy
