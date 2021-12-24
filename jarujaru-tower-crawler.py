import os
import time
from apiclient.discovery import build

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
JARUJARU_TOWER_PLAYLIST_ID = 'PLRdiaanKAFQliJh8AMvlV6t7NBrmNXCo-'

youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)

next_page_token = None

while True:
    playlist_items_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=JARUJARU_TOWER_PLAYLIST_ID,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for i in range(len(playlist_items_response['items'])):
        video_id = playlist_items_response['items'][i]['snippet']['resourceId']['videoId']
        published_at = playlist_items_response['items'][i]['snippet']['publishedAt']
        title = playlist_items_response['items'][i]['snippet']['title']
        print(f'{video_id}, {published_at}, {title}')

    if 'nextPageToken' in playlist_items_response.keys():
        next_page_token = playlist_items_response['nextPageToken']
    else:
        break

    time.sleep(3)