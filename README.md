
HeXacamu is a cross-platform OSINT (Open Source Intelligence) tool designed to collect and organize publicly available data from Instagram, YouTube, and X (formerly Twitter).

✨ Features

🔍 Instagram Scraper

Extracts post images from public profiles (requires manual cookie input).

Creates an HTML gallery with all retrieved images.

Downloads profile pictures.

📺 YouTube Scraper

Fetches all video URLs from a YouTube channel or playlist using yt-dlp.

Saves the video links to a local .txt file.

🐦 X / Twitter Scraper

Uses the Twitter API (v2) to retrieve media URLs from a user's timeline.

Saves the media links in a timestamped .txt file.

📆 Modules & Requirements

This tool uses the following libraries:

instaloader

requests

beautifulsoup4

yt-dlp

tweepy

pyfiglet

Installation

Install dependencies via pip:

pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet tweepy

⚠️ Note

This tool may require manual authentication (e.g. cookies for Instagram or a Bearer Token for X). Please use it responsibly and comply with the terms of service of each platform.

Made for educational and research purposes only.
Use at your own risk.
