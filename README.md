# 🕵️‍♂️ HeXacamu OSINT Tool

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/github/stars/yourusername/hexacamu?style=social" alt="GitHub stars">
</p>

> A multi-platform Open Source Intelligence (OSINT) tool for extracting public media and data from Instagram, YouTube, and X (formerly Twitter). Ideal for research, analysis, and media archiving.

---

## 🔧 Features

- 📷 **Instagram**:
  - Extracts image URLs using GraphQL endpoints
  - Builds a clean offline HTML gallery of posts
  - Downloads high-quality profile pictures

- 📺 **YouTube**:
  - Extracts all video URLs from a channel or playlist using `yt-dlp`
  - Saves results to a text file for easy processing

- 🐦 **Twitter/X**:
  - Pulls media links from public user profiles via Bearer Token
  - Handles rate-limits and authentication gracefully
  - Saves timestamped logs of retrieved media

---

## 📦 Installation

Install required packages with:

```bash
pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet tweepy
