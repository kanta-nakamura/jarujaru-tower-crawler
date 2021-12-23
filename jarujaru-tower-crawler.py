import os
from apiclient.discovery import build

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
JARUJARU_TOWER_PLAYLIST_ID = 'PLRdiaanKAFQliJh8AMvlV6t7NBrmNXCo-'

youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)

playlist_items_response = youtube.playlistItems().list(
    part='snippet',
    playlistId=JARUJARU_TOWER_PLAYLIST_ID,
    maxResults=50
).execute()

print(playlist_items_response)