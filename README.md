# jarujaru-tower-crawler

- ジャルジャルタワーの動画情報をcsvとして取得するクローラー
- 取得先: https://www.youtube.com/playlist?list=PLRdiaanKAFQliJh8AMvlV6t7NBrmNXCo-

## 実行方法

```
$ brew install forego
$ pip install -r requirements.txt
$ echo "YOUTUBE_API_KEY=[youtubeのAPIキー]" > .env
$ forego run python jarujaru-tower-crawler.py > output.csv
```
youtubeのAPIキー取得: https://console.developers.google.com/apis/credentials?hl=ja

## 取得情報

|列名|内容|
|---|---|
|video_id|YouTubeが動画を一意に識別するために使用するID|
|published_at|動画がアップロードされた日時<br>値はISO8601（YYYY-MM-DDThh：mm：ss.sZ）形式で指定|
|title|動画のタイトル|
|comment_count|動画のコメント数|
|view_count|動画の再生数|
|like_count|動画のlike数|
|duration|動画の長さ|

その他取得可能な情報一覧: https://developers.google.com/resources/api-libraries/documentation/youtube/v3/python/latest/youtube_v3.videos.html#list
