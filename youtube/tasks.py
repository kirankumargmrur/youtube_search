from googleapiclient.discovery import build
import googleapiclient
from youtube.models import YoutubeVideos
from django.conf import settings
from datetime import datetime, timedelta
import logging
from fampay_test.celery import app

logger = logging.getLogger()
logger.setLevel(logging.INFO)

response_code = ''
youtube_api_svc_name = 'youtube'
youtube_api_version = 'v3'

@app.task
def get_data():
    logger.info("Data fetching started")
    apiKeys = settings.GOOGLE_API_KEYS
    time_now = datetime.now()
    last_request_time = time_now - timedelta(minutes=5)
    is_key_valid = False

    for apiKey in apiKeys:
        logger.info("Using the key {}".format(apiKey))
        try:
            youtube = build(youtube_api_svc_name, youtube_api_version, developerKey=apiKey)
            search = youtube.search().list(q=settings.QUERY_STRING, part="id, snippet", order="date", maxResults=20,
                                           publishedAfter=(last_request_time.replace(microsecond=0).isoformat() + 'Z'))
            search_response = search.execute()
            is_key_valid = True
        except googleapiclient.errors.HttpError as err:
            response_code = err.resp.status
            logger.error("ERROR: {}".format(err))
            if not (response_code == 400 or response_code == 403):
                break

        if is_key_valid:
            break

    if is_key_valid:
        for item in search_response.get('items', []):
            if item['id']['kind'] == 'youtube#video':
                title = item['snippet']['title']
                description = item['snippet']['description']
                video_id = item['id']['videoId']
                published = item['snippet']['publishedAt']
                thumbnail_urls = item['snippet']['thumbnails']['default']['url']
                channel = item['snippet']['channelTitle']
                logger.info("Adding {} video data to table".format(title))
                YoutubeVideos.objects.create(
                    title=title,
                    description=description,
                    video_id=video_id,
                    channel=channel,
                    published=published,
                    thumbnail_urls=thumbnail_urls)