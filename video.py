from utils import call_api
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

def get_all_comments_on_video(video_id):
    api_url = "https://www.googleapis.com/youtube/v3/commentThreads"

    # Define the custom parameters
    params = {
        "key": api_key,  # Replace with your API key
        "part": "snippet,replies",
        "videoId": video_id,
        "maxResults": 100  # Maximum comments per page
    }

    comments = []

    response = call_api(api_url, params)

    if response:
        # Process the current page of comments
        for item in response.get("items", []):
            comment_data = {
                "text": item['snippet']['topLevelComment']['snippet']['textDisplay'],
                "author": item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                "authorImage": item['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
                "authorChannel": item['snippet']['topLevelComment']['snippet']['authorChannelUrl']
            }
            comments.append(comment_data)

        # Check if there is a next page
    else:
        print("Failed to fetch the API response.")
    return comments

def get_video_stats(video_id):
    api_url = "https://www.googleapis.com/youtube/v3/videos"

    # Define the custom parameters
    params = {
        "key": api_key,  # Replace with your API key
        "part": "snippet,contentDetails,statistics",
        "id": video_id
    }

    # Call the API
    response = call_api(api_url, params)

    if response and "items" in response and len(response["items"]) > 0:
        video_data = response["items"][0]

        # Extract desired information
        video_stats = {
            "publishedAt": video_data["snippet"]["publishedAt"],
            "title": video_data["snippet"]["title"],
            "description": video_data["snippet"].get("description", ""),
            "channelTitle": video_data["snippet"]["channelTitle"],
            "viewCount": int(video_data["statistics"].get("viewCount", 0)),
            "likeCount": int(video_data["statistics"].get("likeCount", 0)),
            "commentCount": int(video_data["statistics"].get("commentCount", 0)),
            "duration": video_data["contentDetails"]["duration"],
            "tags": video_data["snippet"].get("tags", [])
        }

        return video_stats
    else:
        print("Failed to fetch the API response.")
        return None
 