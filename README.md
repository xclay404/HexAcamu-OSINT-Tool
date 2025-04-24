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

# HexaCamu - Social Media Web Crawler

**HexaCamu** is a web crawler for Instagram (and later it will work on various social media platforms) which downloads the profile picture and every post.

## 📑 Table of Contents
- [Project Description](#project-description)
- [How it Works](#how-it-works)
  - [Instagram](#instagram)
  - [YouTube](#youtube)
  - [X / Twitter / TWIX](#x-twitter-twix)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Disclaimer](#disclaimer)

## 📜 Project Description

HexaCamu is a web crawler that is currently developed for Instagram and will be extended to other social platforms in the future. It allows downloading the profile picture and all posts of an Instagram profile.

Currently, HexaCamu supports the following platforms:

- **Instagram**: Download profile pictures and posts.
- **YouTube**: Download all video URLs of a channel or playlist.
- **X/Twitter**: (Future feature)

## ⚙️ How it Works

### Instagram

1. **Fetching the Instagram Gallery**:
   - The user needs to provide essential cookies like `csrftoken` (session and authentication data) to access Instagram.
   - HexaCamu uses the `Instaloader` library to attempt fetching an Instagram profile's posts. If the request is blocked, the script extracts the necessary GraphQL query URL from the error message.
   - The image URLs are then saved to a text file and used to generate a simple HTML gallery. This gallery is automatically opened in a browser for the user to view.

2. **Hexacamu allows the user to download the profile picture**:
   - It does so by scraping the page for the `og:image` meta tag (which contains the URL of the profile picture) and downloads the image to the local file system.

### YouTube

- **Download all Videos / URLs of a certain Channel or Playlist**:
   - With HexaCamu, you can download all video URLs from a YouTube channel or playlist and save them locally.

### X / Twitter / TWIX

- **Future Support**:
   - In future versions, HexaCamu will also be able to extract media URLs from Twitter (X). The crawler will then be able to download tweets and media (images, videos) from a specific Twitter user.

## 💻 Installation

### Prerequisites

1. Install the required Python packages:
   ```bash
   pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet


## 📦 Installation

Install required packages with:

```bash
pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet tweepy
