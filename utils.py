import re
import requests
from urllib.parse import urlparse, parse_qs

def call_api(api_url, params):
    """
    Calls an API with the specified URL and parameters.

    :param api_url: str - The base URL of the API.
    :param params: dict - A dictionary of parameters to include in the request.
    :return: dict - The JSON response from the API.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_channel_username(channel_url):
    """
    Extracts the channel username from various YouTube URL formats.

    :param channel_url: str - The URL of the YouTube channel.
    :return: str - The extracted username or an error message.
    """
    # Regular expressions for different YouTube URL formats
    channel_pattern = r'https?://www\.youtube\.com/@([^/?]+)'  # Custom channel URL
    legacy_channel_pattern = r'https?://www\.youtube\.com/(?:user|c)/([^/?]+)'  # Legacy and custom URLs
    standard_channel_pattern = r'https?://www\.youtube\.com/channel/([^/?]+)'  # Channel ID format
    c_channel_pattern = r'https?://www\.youtube\.com/c/([^/?]+)'  # Custom name format

    # Check each pattern to find a match
    match = re.match(channel_pattern, channel_url)
    if match:
        return match.group(1)  # Return the username from custom URL

    match = re.match(legacy_channel_pattern, channel_url)
    if match:
        return match.group(1)  # Return the username from legacy URL

    match = re.match(standard_channel_pattern, channel_url)
    if match:
        return "Channel ID format does not provide a username."

    match = re.match(c_channel_pattern, channel_url)
    if match:
        return match.group(1)  # Return the custom name from /c/ format

    return "Invalid YouTube channel URL."

def extract_search_query(url):
    # Parse the URL and extract the search query
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('search_query', [None])[0]

def extract_playlist_id(playlist_url):
    # Regular expression to extract playlist ID from the URL
    pattern = r'list=([^&]+)'
    match = re.search(pattern, playlist_url)
    return match.group(1) if match else None
