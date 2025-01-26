# YouTube URL Scraper

## Overview
The **YouTube URL Scraper** is a Python-based application designed to scrape data from various types of YouTube URLs. It provides a simple interface to extract valuable information for videos, playlists, search results, and channel home pages.

---

## Features
The scraper supports the following YouTube URL types:

- **Video URL**: Extracts metadata about a specific video, including title, description, likes, views,the top comments(text,author etc of each comment) and more.
- **Playlist**: Retrieves information about all videos in a given playlist, such as video titles.
- **Search Result**: Scrapes data from YouTube search results, such as video links, titles, and snippets.
- **Channel Home Page**: Gathers details about a channel, including its name, subscriber count, and video list.

---
## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/TeekshaHarish/YouTube-URL-Scraper
   cd youtube-url-scraper
   ```
2. Install the required dependencies:
   ```bash
   pip install python-dotenv requests
   ```
3. Configure the .env file and add your API key for youtube data api v3.
   ```bash
   API_KEY="your_api_key"
   ```
4. Run the main script:
    ```bash
   python main.py
   ```
5. Input the YouTube URL when prompted to begin scraping.

---
## How It Works

1. URL Input: The user provides a YouTube URL of the following types:
   - Video URL
   - Playlist URL
   - Search Results
   - Channel Home Page

2. Scraper Identification:
   The application identifies the type of URL using patterns and rules.

3. Data Extraction:
   Scrapes metadata such as titles, descriptions, likes, views, or subscriber counts using tools like BeautifulSoup or APIs like the YouTube Data API.

4. Output Delivery:
   Displays the scraped data on the console.
