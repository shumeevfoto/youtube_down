import googleapiclient.discovery

KEY = 'AIzaSyC6RhmFJXLOii4_dP2iBZ9B5XQErhbEqMQ'
# CHANEL_NAME = 'UClD6ycrH9jBkNzQkXup7A5w'
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=KEY)


def yotube_result(res):
    playlist = youtube_get_kay(res)
    responce = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist,
        maxResults=30
    ).execute()
    ids = []
    for video in responce['items']:
        ids.append(video['snippet']['resourceId']['videoId'])
    return ids


def playlist_video_id(videos):
    responce = youtube.videos().list(
        part="statistics,snippet",
        id=(',').join(videos)
    ).execute()
    for video in responce["items"]:
        print("Название канала: " + video['snippet']['title'])
        print("Просмотры: " + video['statistics']['viewCount'])
        print("Лайки: " + video['statistics']['likeCount'])
        print('-----------------------------')


def youtube_get_kay(chanel_name):
    responce = youtube.channels().list(
        part="contentDetails",
        id=chanel_name
    ).execute()
    print(responce)
    return responce['items'][0]['contentDetails']['relatedPlaylists']['uploads']