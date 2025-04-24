import instaloader
import re
import time
import requests
import os
import webbrowser
from bs4 import BeautifulSoup
import subprocess 
import tweepy
from datetime import datetime
import pyfiglet

# requirements
# || pip install instaloader requests beautifulsoup4 yt-dlp pyfiglet|| 



def ascii_banner():
    banner = pyfiglet.figlet_format("HeXacamu      OSINT Tool ")
    print(banner)

ascii_banner()



def NULL_messages():
    response = requests.get("https://example.com")  
    if response.status_code != 200:
        print(f"Error with code {response.status_code} occurred, lmao loser")
    else:
        SystemExit()

def instagram():
    def get_cookies():
        print("Feed me with cookies please:")
        cookies = {
            "csrftoken": input("csrftoken: ").strip(),
            "datr": input("datr: ").strip(),
            "dpr": input("dpr: ").strip(),
            "ds_user_id": input("ds_user_id: ").strip(),
            "ig_did": input("ig_did: ").strip(),
            "ig_direct_region_hint": input("ig_direct_region_hint: ").strip(),
            "mid": input("mid: ").strip(),
            "rur": input("rur: ").strip(),
            "sessionid": input("sessionid: ").strip(),
            "wd": input("wd: ").strip()
        }
        return cookies

    def extract_graphql_url(error_message):
        graphql_url_pattern = r"https://www.instagram.com/graphql/query\?variables=.*?&doc_id=\d+"
        match = re.search(graphql_url_pattern, error_message)
        if match:
            return match.group(0)
        return None

    def fetch_profile_graphql_url(profile_name):
        try:
            L = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(L.context, profile_name)
            print(f"Fetching profile for {profile.username}...")
            raise Exception("JSON Query to graphql/query: 401 Unauthorized - forced error for URL extraction")
        except Exception as e:
            error_message = str(e)
            graphql_url = extract_graphql_url(error_message)
            if graphql_url:
                with open("graphql_url.txt", "w") as file:
                    file.write(graphql_url)
                print(f"GraphQL URL saved: {graphql_url}")
                return graphql_url
            else:
                raise Exception("Failed to extract GraphQL URL from error message")

    def fetch_image_urls(graphql_url, profile_name):
        cookies = get_cookies()
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Referer": "https://www.instagram.com/"
        }

        print(f"Fetching: {graphql_url}")
        res = requests.get(graphql_url, headers=headers, cookies=cookies)

        if res.status_code == 200:
            user_folder = f"./{profile_name}_gallery"
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)

            with open(os.path.join(user_folder, "response.json"), "w", encoding="utf-8") as f:
                f.write(res.text)

            image_urls = re.findall(r'"url":"(https://[^\"]+\.jpg.*?)"', res.text)
            decoded_urls = [url.encode('utf-8').decode('unicode_escape') for url in image_urls]

            with open(os.path.join(user_folder, "image_urls.txt"), "w", encoding="utf-8") as f:
                for url in decoded_urls:
                    f.write(url + "\n")

            return decoded_urls
        else:
            print(f"Failed: HTTP {res.status_code}")
            return []

    def create_gallery_with_urls(image_urls, profile_name):
        user_folder = f"./{profile_name}_gallery"
        html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset=\"UTF-8\">
    <title>Instagram Gallery</title>
    <style>
        body { background: #111; color: #eee; font-family: sans-serif; text-align: center; }
        .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 20px; }
        img { max-width: 300px; max-height: 300px; object-fit: cover; border-radius: 8px; box-shadow: 0 0 8px #333; }
    </style>
</head>
<body>
    <h1>Instagram Image Gallery</h1>
    <div class=\"container\">
"""
        for url in image_urls:
            html_content += f'        <img src="{url}" alt="Instagram Image">\n'

        html_content += """    </div>
</body>
</html>"""

        html_file_path = os.path.join(user_folder, "gallery.html")
        with open(html_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        webbrowser.open(f"file://{os.path.abspath(html_file_path)}")

    def get_instagram_profile_pic():
        username = input("Enter Instagram username (for the pfp):")
        url = f"https://www.instagram.com/{username}/"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error while loading the site: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        og_image = soup.find("meta", property="og:image")
        if og_image:
            image_url = og_image["content"]
            print(f"Pfp-URL: {image_url}")

            img_data = requests.get(image_url).content
            filename = f"{username}_pfp.jpg"
            with open(filename, "wb") as f:
                f.write(img_data)
            print("Pfp saved as:", filename)
        else:
            print("Pfp not found")

    try:
        profile_name = input("Enter Instagram username (for posts): ").strip()
        graphql_url = fetch_profile_graphql_url(profile_name)
        image_urls = fetch_image_urls(graphql_url, profile_name)
        if image_urls:
            create_gallery_with_urls(image_urls, profile_name)
        else:
            print("No image URLs found to create gallery.")
    except Exception as e:
        print(f"Error: {e}")

    get_instagram_profile_pic()

def youtube():
    
        url = input("Enter the URL of a YouTube channel or playlist: ").strip()

        print("\nFetching channel name...")

        try:
            # Get the channel name using yt-dlp
            name_result = subprocess.run(
                ["python", "-m", "yt_dlp", "--print", "%(channel)s", "--skip-download", "--flat-playlist", url],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            channel_name = name_result.stdout.strip().split('\n')[0]
            if not channel_name:
                print(" No channel name found – using fallback.")
                channel_name = "unknown_channel"

        except Exception as e:
            print(f"Error while fetching channel name: {e}")
            return

        # Remove invalid characters
        channel_name = re.sub(r'[\\/*?:"<>|]', "_", channel_name)
        filename = f"youtube_URLs_{channel_name}.txt"

        print(f"\nCollecting video URLs from channel: {channel_name}...\n")

        result = subprocess.run(
            ["python", "-m", "yt_dlp", "--flat-playlist", "--print", "%(url)s", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print("Error while retrieving video URLs:")
            print(result.stderr)
            return

        video_ids = result.stdout.strip().split("\n")
        full_urls = [f"https://www.youtube.com/watch?v={vid}" for vid in video_ids]

        with open(filename, "w", encoding="utf-8") as f:
            for video_url in full_urls:
                f.write(video_url + "\n")

        print(f"\n{len(full_urls)} video URLs were saved to '{filename}'.")

def twitter():
    

    def fetch_user_media(username, bearer_token, max_tweets=100):
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
            if hasattr(e, "response") and e.response and hasattr(e.response, "status_code"):
                if e.response.status_code == 401:
                    print("401 Unauthorized. Check your Bearer Token.")
                elif e.response.status_code == 429:
                    print("Rate limit hit. Try again later.")
                else:
                    print(f"Error for @{username}: {e}")
            else:
                print(f"Tweepy error: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def save_media_urls(username, bearer_token, output_dir="media_links"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"{username}_media_{timestamp}.txt")
        media_urls = fetch_user_media(username, bearer_token)
        if not media_urls:
            print(f"No media for @{username} or SOME ERROR IDK HOW TO SOLVE.")
            return
        with open(output_file, 'w', encoding='utf-8') as f:
            for url in media_urls:
                f.write(url + '\n')
        print(f"Saved media URLs to {output_file}")

    # Main block
    bearer_token = input("Enter your X Bearer Token (you need to log in at the X API page): ").strip()
    if not bearer_token:
        print("Bearer Token can't be empty.")
        return
    username = input("Enter X username (without @): ").strip()
    if not username:
        print("Username can't be empty.")
        return
    save_media_urls(username, bearer_token)


def main():
    while True:
        try:
            choose_platform = input("Choose either A for Instagram or B for YouTube, C for X / Twitter: ")
            if choose_platform.lower() == "a":
                instagram()
                break
            elif choose_platform.lower() == "b":
                youtube()
                break
            elif choose_platform.lower() == "c":
                twitter()
                break
            else:
                print("Invalid input, you did not choose between A, B or C. Try again.")
        except ValueError:
            NULL_messages()
            break

if __name__ == "__main__":
    main()
