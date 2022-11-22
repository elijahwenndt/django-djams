from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import * 
from .serializers import * 
from rest_framework.response import Response
# Create your views here.

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ReadSongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = ReadSongSerializer
    http_method_names = ['get']

    # def update(self, request, pk=None, *args, **kwargs):
    #     song_update = Song.objects.get(pk=pk)
    #     data = request.data
    #     serializer= SongSerializer(instance=song_update, data=data, partial=True)

    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     response = Response()

    #     return response


    # def create(self, request, args, **kwargs):
    #     data = request.data

    #     new_song = Song.objects.create(title=data["title"], duration=data['duration'], plays=['plays'], explicit=['explicit'])
    #     new_song.save()

    #     for album in data["album"]:


 
        

      