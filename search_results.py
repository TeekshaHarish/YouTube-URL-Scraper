from utils import call_api
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def search_youtube(query, max_results=10):
    # Define the API endpoint
    api_url = "https://www.googleapis.com/youtube/v3/search"

    # Prepare parameters for API request
    params = {
        "key": api_key,
        "part": "snippet",
        "q": query,
        "maxResults": max_results,
        "type": "video"  # We are only interested in video results
    }

    response = call_api(api_url, params)
    
    if response:
        videos = []
        # Extract video details from the response
        for item in response.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            publishedAt = item["snippet"]["publishedAt"]
            channelTitle = item["snippet"]["channelTitle"]
            videos.append({"title": title, "videoId": video_id,"publishedAt":publishedAt,"channel":channelTitle})

        return videos
    else:
        print("Error fetching data:", response)
        return None
