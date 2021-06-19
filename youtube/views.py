from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import TemplateView, ListView
from youtube.serializers import *
from rest_framework import generics
from rest_framework.pagination import CursorPagination
from rest_framework import filters
from django.http import HttpResponseRedirect


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class PaginationResponse(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100


class GetApiView(generics.ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['channel']
    ordering = '-published'
    queryset = YoutubeVideos.objects.all()
    serializer_class = YoutubeVideosSerializer
    pagination_class = PaginationResponse


class SearchApiView(generics.ListAPIView):
    model = YoutubeVideos
    serializer_class = YoutubeVideosSerializer
    pagination_class = PaginationResponse
    context_object_name = 'search_api_results'
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['channel']
    ordering = ('-published')

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return YoutubeVideos.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)).order_by('-published').distinct()

        return YoutubeVideos.objects.all()


class SearchView(ListView):
    model = YoutubeVideos
    template_name = 'search.html'
    context_object_name = 'video'
    serializer_class = YoutubeVideosSerializer
    pagination_class = PaginationResponse
    context_object_name = 'search_results'
    fields = YoutubeVideos._meta.get_fields()

    def get_queryset(self):
        query = self.request.GET.get("q")
        filter_query = self.request.GET.get("filterQ")
        sorting_element = self.request.GET.get("sortby")
        sort_order = self.request.GET.get("sortorder")
        if sorting_element is not None:
            if 'desc' == sort_order:
                sorting_element = '-{}'.format(sorting_element)
        else:
            sorting_element = '-published'

        if query:
            query_list = query.split(' ')
            for item in query_list:
                return YoutubeVideos.objects.filter(
                    Q(title__icontains=item) | Q(description__icontains=item)).order_by(sorting_element).distinct()
        if filter_query:
            return YoutubeVideos.objects.filter(
                Q(title__icontains=filter_query) | Q(description__icontains=filter_query) ).order_by(sorting_element).distinct()

        return YoutubeVideos.objects.all().order_by(sorting_element)


class WatchView(ListView):

    def get_queryset(self):
        query = self.request.GET.get("url")

        if query:
            return HttpResponseRedirect("http://google.com")
