from django.db import models


# Create your models here.
class YoutubeVideos(models.Model):
    title = models.CharField(null=True, blank=True, max_length=500)
    description = models.CharField(null=True, blank=True, max_length=5000)
    video_id = models.CharField(null=False, blank=False, max_length=200, primary_key=True)
    published = models.DateTimeField()
    thumbnail_urls = models.URLField()
    channel = models.CharField(null=True, blank=True, max_length=500)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
