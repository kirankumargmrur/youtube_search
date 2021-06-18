from rest_framework import serializers
from youtube.models import YoutubeVideos


class YoutubeVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideos
        fields = "__all__"
