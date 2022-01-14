from pytube import YouTube
import ffmpeg
import googleapiclient.discovery
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import youtube_dl

KEY = 'AIzaSyC6RhmFJXLOii4_dP2iBZ9B5XQErhbEqMQ'
URL = 'https://youtu.be/W-IoqVVRVrs'
U = 'Cn0sMvgqf4E'
DIRECTORY = 'Download'
CHANEL_NAME = 'UCYEA2g99DBNPhNuXJdhOJ7Q'
api_service_name = "youtube"
api_version = "v3"
BOTDER_TIME = 86400

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=KEY)


def get_youtube_piple(url):
    global metap
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    pipls = soup.select('div.watch-main-col meta')
    print(pipls)
    metatags = soup.find_all('meta', attrs={'itemprop': 'interactionCount'})
    for metap in metatags:
        print(metap)
    print(metap.attrs['content'])
    return metap.attrs['content']


def get_youtube_title(url):
    yt = YouTube(url)
    title_video = yt.title
    print(title_video)
    return title_video


def get_youtube_thumb(url):
    yt = YouTube(url)
    thumb_video = yt.thumbnail_url
    print(thumb_video)
    return thumb_video


def get_yotybe_360(url):
    global stream
    yt = YouTube(url)
    stream_video_360 = yt.streams.filter(file_extension='mp4', res="360p", progressive=True)
    for stream in stream_video_360:
        stream.download(filename='video.mp4')


def get_yotybe_720(url):
    yt = YouTube(url)
    stream_video_720 = yt.streams.filter(file_extension='mp4', res="720p", progressive=True)

    for stream in yt.streams:
        print(stream)


def get_audio(url):
    global stream
    yt = YouTube(url)
    stream_audio = yt.streams.get_audio_only()
    stream_audio.download(filename='audio.mp4')

def get_yotybe_hd(url):
    yt = YouTube(url)
    stream_video_hd = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
    print(stream_video_hd)


def to_valid(url):
    youtube1, VID_ID = url.split('=', maxsplit=1)
    if youtube1.startswith('http://') or youtube1.startswith('https://') or youtube1.startswith('www.') \
            or youtube1.startswith('youtu'):
        print(VID_ID)
        return VID_ID

def to_valid_test(url):
    youtube_urls_test = ['']
    youtube_urls_test.pop(0)
    youtube_urls_test.append(url)
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    VID_ID = youtube_regex_match.group(6)
    if youtube_regex_match != None:
        print(VID_ID)
        return VID_ID

    else:
        print('NO Valid')
        raise Exception('NOT_VALID_URL')


def to_valid_vid(url):
    youtube1, VID_ID = url.split('=', maxsplit=1)
    VID_ID = VID_ID + '.mp4'
    print(youtube1, VID_ID)
    # VID_ID = youtube_regex_match.group(6)
    # if youtube_regex_match != None:
    #     return VID_ID
    # else:
    #     print('NO Valid')
    #     raise Exception('NOT_VALID_URL')


def worker(VID_ID):
    ydl_opts = {
        'max_filesize': 20000000000,
        'format': 'best',
        'outtmpl': VID_ID + '.mp4',
        'output': VID_ID + '.mp4',
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([VID_ID])


#     stream_video.download(DIRECTORY,'video.mp4')
#     if not stream_video.is_progressive:
#         stream_audio = yt.streams.get_audio_only()
#         stream_audio.download(DIRECTORY,'audio.mp4')
#     combine(DIRECTORY + '/audio.mp4', DIRECTORY + '/video.mp4')
#
# def combine(audio, video):
#     stream_audio = ffmpeg.input(audio)
#     stream_video = ffmpeg.input(video)
#     ffmpeg.output(stream_audio, stream_video, DIRECTORY + '/result.mp4').run()

#
#
if __name__ == "__main__":
    # yotube_result(CHANEL_NAME)
    # get_yotybe_360(URL)
    #to_valid_vid(URL)
    # get_youtube_title(URL)
    # get_youtube_thumb(URL)
    # get_youtube_piple(URL)
    #worker(U)
    #get_yotybe_720(URL)
    to_valid_test(URL)
