import os
import time
from apiclient.discovery import build

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
JARUJARU_TOWER_PLAYLIST_ID = 'PLRdiaanKAFQliJh8AMvlV6t7NBrmNXCo-'

youtube = build('youtube', 'v3', developerKey = YOUTUBE_API_KEY)

next_page_token = None

print('video_id,published_at,title,comment_count,view_count,like_count,duration')

while True:
    playlist_items_response = youtube.playlistItems().list(
        part='snippet',
        playlistId=JARUJARU_TOWER_PLAYLIST_ID,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    for i in range(len(playlist_items_response['items'])):
        video_id = playlist_items_response['items'][i]['snippet']['resourceId']['videoId']

        video_response = youtube.videos().list(
            part=['snippet', 'statistics', 'contentDetails'],
            id=video_id
        ).execute()
        
        if len(video_response) > 0:
            published_at = video_response['items'][0]['snippet']['publishedAt']
            title = video_response['items'][0]['snippet']['title']
            comment_count = video_response['items'][0]['statistics']['commentCount']
            view_count = video_response['items'][0]['statistics']['viewCount']
            like_count = video_response['items'][0]['statistics']['likeCount']
            duration = video_response['items'][0]['contentDetails']['duration']

            values = [video_id
                    ,published_at
                    ,title
                    ,comment_count
                    ,view_count
                    ,like_count
                    ,duration]
            
            print(','.join(values))

        time.sleep(3)

    if 'nextPageToken' in playlist_items_response.keys():
        next_page_token = playlist_items_response['nextPageToken']
    else:
        break

    time.sleep(3)