import re
from utils import extract_playlist_id,extract_search_query
from channel_details import home
from search_results import search_youtube
from playlist import fetch_videos_in_playlist
from video import get_all_comments_on_video,get_video_stats

def extract_info(url):
    video_pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([^&?]{11})'
    channel_pattern = r'https?://www\.youtube\.com/@[^/?]+'
    legacy_channel_pattern = r'https?://www\.youtube\.com/(?:user|c)/[^/?]+'
    standard_channel_pattern = r'https?://www\.youtube\.com/[^/?]+$'
    playlist_pattern = r'https?://www\.youtube\.com/playlist\?list=[^&]+'
    search_pattern = r'https?://www\.youtube\.com/results\?search_query=.*'

    if re.match(video_pattern, url):
        return "video"
    elif re.match(channel_pattern, url) or re.match(legacy_channel_pattern, url) or re.match(standard_channel_pattern, url):
        return "channel"
    elif re.match(playlist_pattern, url):
        return "playlist"
    elif re.match(search_pattern, url):
        return "search"
    else:
        return "unknown"

def process_url(url):
    url_type = extract_info(url)
    print("\n--- URL Analysis ---")
    print(f"URL: {url}")
    print(f"Type: {url_type.capitalize()} URL\n")

    if url_type == "video":
        video_id = re.search(r'(?<=v=)[^&]+', url).group() if 'v=' in url else url.split('/')[-1]
        details = get_video_stats(video_id)
        if details:
            print("Video Details:")
            for key, value in details.items():
                print(f"  {key.capitalize()}: {value}")
            print("\n")
        comments = get_all_comments_on_video(video_id)
        if comments:
            print("Top Comments on Video:")
            for comment in comments:
                for key, value in comment.items():
                    print(f"  {key.capitalize()}: {value}")
                print("")
    elif url_type == "channel":
        # print("This is a YouTube Channel URL.\n")
        channel_data=home(url)
        for key, value in channel_data.items():
            print(f"  {key.capitalize()}: {value}")
        # Additional channel handling can be added here.
    elif url_type == "playlist":
        playlist_id = extract_playlist_id(url)
        if playlist_id:
            videos = fetch_videos_in_playlist(playlist_id)
            print(f"Playlist contains {len(videos)} videos:")
            for video in videos:
                print(f"  Title: {video['title']} | Video ID: {video['videoId']}")
    elif url_type == "search":
        search_query = extract_search_query(url)
        if search_query:
            print(f"Search Query: {search_query}")
            top_videos = search_youtube(search_query)
            print("Top Search Results:")
            for video in top_videos:
                print(f"  Title: {video['title']} | Video ID: {video['videoId']} | Channel: {video['channel']} | Published: {video['publishedAt']}")
                print()
    else:
        print("This URL type is not recognized.")

def main():
    try:
        url = input("Enter a YouTube URL: ").strip()
        process_url(url)
    except:
        print("Some error occured please enter a valid url and try again!")

if __name__ == "__main__":
    main()
