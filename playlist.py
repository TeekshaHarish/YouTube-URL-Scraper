from utils import call_api
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def fetch_videos_in_playlist(playlist_id):
    # Define the API endpoint
    api_url = "https://www.googleapis.com/youtube/v3/playlistItems"
    
    # Prepare parameters for API request
    params = {
        "key": api_key,
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": 50  # Maximum number of results per request
    }
    
    videos = []
    
    while True:
        response = call_api(api_url, params)
        if response:
            # Extract video details from the response
            for item in response.get("items", []):
                video_title = item["snippet"]["title"]
                video_id = item["snippet"]["resourceId"]["videoId"]
                videos.append({"title": video_title, "videoId": video_id})
            
            # Check for next page token
            if "nextPageToken" in response:
                params["pageToken"] = response["nextPageToken"]
            else:
                break  # Exit loop if there are no more pages
        else:
            print("Error fetching data:", response)
            break
    
    return videos
