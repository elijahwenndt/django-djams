from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Artist, Album, Playlist, Genre, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = ['title', 'duration', 'genre', 'album', 'artist', 'plays', 'explicit', 'playlist']

        