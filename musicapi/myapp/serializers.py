from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Artist, Album, Playlist, Genre, Song

class ArtistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class PlaylistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class SongSerializers(serializers.ModelSerializer):
    genre = GenreSerializer()
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = ['title', 'duration', 'genre', 'album', 'artist', 'plays', 'explicit', 'playlist']