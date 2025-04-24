# 🕵️‍♂️ HeXacamu OSINT Tool

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  <img src="https://img.shields.io/github/stars/yourusername/hexacamu?style=social" alt="GitHub stars">
</p>

> A multi-platform Open Source Intelligence (OSINT) tool for extracting public media and data from Instagram, YouTube, and X (formerly Twitter). Ideal for research, analysis, and media archiving.

---


# HexaCamu - Social Media Web Crawler

**HexaCamu** is a web crawler for Instagram, YouTube and X / Twitter (and later it will work on various social media platforms) which provides us with further information about a certain account of your wish! 

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
## 📜 Project Description

HexaCamu is a web crawler that is currently developed for Instagram and will be extended to other social platforms in the future. It allows downloading the profile picture and all posts of an Instagram profile.

Currently, HexaCamu supports the following platforms:

- **Instagram**: 
- **YouTube**: 
- **X/Twitter**: 

## ⚙️ How it Works

### Instagram

Which cookies do I need to fill in there and how can I find them? 

Just by going into developer mode ( mostly by pressing F12 ), you can see a section named ' Cookies ' and there you go. 

1. **Fetching the Instagram Gallery**:
   - The user needs to provide essential cookies like `csrftoken` (session and authentication data) to access Instagram.
   - HexaCamu uses the `Instaloader` library to attempt fetching an Instagram profile's posts. If the request is blocked, the script extracts the necessary GraphQL query URL from the error message.
   - The image URLs are then saved to a text file and used to generate a simple HTML gallery. This gallery is automatically opened in a browser for the user to view.

2. **Hexacamu allows the user to download the profile picture**:
   - It does so by scraping the page for the `og:image` meta tag (which contains the URL of the profile picture) and downloads the image to the local file system.

### YouTube

- **Download all Videos / URLs of a certain Channel or Playlist**:
   - With HexaCamu, you can download all video URLs from a YouTube channel or playlist and save them locally.

### X / Twitter

1. **Fetching user media URLs**:
   - The user provides their X (formerly Twitter) username and a Bearer Token (required for API access).
   - HexaCamu uses the `tweepy` library to fetch media URLs from a user's tweets.
   - It collects media URLs from up to 100 tweets and saves them in a `.txt` file.

2. **Usage of Bearer Token**:
   - The user must input a valid Bearer Token from the X API page to authenticate the request and access the user's tweets.

---

### **Twitter Functionality**

The Twitter functionality in HexaCamu works as follows:

1. **Fetch user media**:
   - The user is prompted to input their X username and Bearer Token.
   - The app fetches the user's media URLs using the X API and the `tweepy` library.
   - It retrieves up to 100 tweets and checks if there are media attached to those tweets (e.g., images, videos).
   
2. **Media saving**:
   - Media URLs are saved in a `.txt` file in a `media_links` directory.
   - The filename is timestamped for each session, ensuring media URLs are saved uniquely each time.

   The function to fetch media URLs is implemented as follows:

   ```python
   def fetch_user_media(username, bearer_token, max_tweets=100):
       # Function to fetch media URLs from a user's tweets
       try:
           client = tweepy.Client(bearer_token=bearer_token)
           user = client.get_user(username=username)
           if not user.data:
               print(f"User @{username} not found or is private.")
               return []
           user_id = user.data.id
           media_urls = []
           tweets = client.get_users_tweets(
               id=user_id,
               max_results=max_tweets,
               tweet_fields=["created_at"],
               media_fields=["url"],
               expansions=["attachments.media_keys"]
           )
           if tweets.data is None:
               print(f"No tweets found for @{username}.")
               return media_urls
           if tweets.includes and "media" in tweets.includes:
               for tweet in tweets.data:
                   if hasattr(tweet, "attachments") and "media_keys" in tweet.attachments:
                       for media_key in tweet.attachments["media_keys"]:
                           for media in tweets.includes["media"]:
                               if media.media_key == media_key and hasattr(media, "url"):
                                   media_urls.append(media.url)
           return media_urls
       except tweepy.TweepyException as e:
           print(f"Error: {e}")
           return []

This functionality allows users to collect media links (images, videos) shared by a user on Twitter and save them to a file for further use.

## 💻 Installation

### Prerequisites

1. Install the required Python packages:
   ```bash
   pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet


```bash

