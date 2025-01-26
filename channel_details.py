from utils import extract_channel_username, call_api
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')


def home(url):
    # Define the API endpoint
    api_url = "https://www.googleapis.com/youtube/v3/channels"
    username=extract_channel_username(url)
    # print(username)
    # Define the custom parameters
    params = {
        "key": api_key,
        "part": "snippet,contentDetails,statistics",
        "forUsername": username
    }

    # Call the API
    response = call_api(api_url, params)
    # print(response)
    if response and "items" in response and len(response["items"]) > 0:
        channel_info = {
            "title": response["items"][0]["snippet"]["title"],
            "description": response["items"][0]["snippet"]["description"],
            "viewCount": response["items"][0]["statistics"]["viewCount"],
            "subscriberCount": response["items"][0]["statistics"]["subscriberCount"],
            "videoCount": response["items"][0]["statistics"]["videoCount"]
        }
        return channel_info
    else:
        print("Failed to fetch the API response.")
        return None
   