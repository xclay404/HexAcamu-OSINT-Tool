🎯 HeXacamu OSINT Tool





HeXacamu is a cross-platform 🔍 OSINT (Open Source Intelligence) tool designed to collect and organize publicly available data from Instagram, YouTube, and X (formerly Twitter).

📚 Table of Contents

✨ Features

🛠️ Installation

📦 Requirements

⚠️ Note

📜 License

✨ Features

📸 Instagram Scraper

  - Extracts post images from public profiles (requires manual cookie input).

  - Creates a responsive HTML gallery.

  - Downloads high-res profile pictures.

📺 YouTube Scraper

🔗 Fetches all video URLs from a channel or playlist using yt-dlp.

📄 Saves URLs in a .txt file.

🐦 X / Twitter Scraper

🧠 Uses the Twitter API v2 to retrieve media from a user's timeline.

💾 Saves media links in a timestamped .txt file.

🛠️ Installation

Install dependencies via pip:

pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet tweepy

📦 Requirements

This tool uses the following libraries:

instaloader

requests

beautifulsoup4

yt-dlp

tweepy

pyfiglet

⚠️ Note

🧪 This tool may require manual authentication (e.g. cookies for Instagram, or a Bearer Token for X). Please use it responsibly and comply with each platform's Terms of Service.

📜 License

This project is licensed under the MIT License.

🧠 Made for educational and research purposes only. Use at your own risk.

