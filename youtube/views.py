from django_filters.rest_framework import DjangoFilterBackend

from youtube.models import YoutubeVideos
from youtube.serializers import *

# Rest FrameWork
from rest_framework import generics
from rest_framework.pagination import CursorPagination
from rest_framework import filters


# Create your views here.

class PaginationResponse(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class GetApiView(generics.ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['channel']
    ordering = ('-published')
    queryset = YoutubeVideos.objects.all()
    serializer_class = YoutubeVideosSerializer
    pagination_class = PaginationResponse
