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
    # genre = GenreSerializer()
    # album = AlbumSerializer(many=True)
    # artist = ArtistSerializer(many=True)
    # playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = ['title', 'duration', 'genre', 'album', 'artist', 'plays', 'explicit', 'playlist']

class ReadSongSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    class Meta:
        model = Song
        fields = "__all__"

    # def create(self, validated_data):
    #     genre_data = validated_data.pop('genre')
    #     album_data = validated_data.pop('album')
    #     artist_data = validated_data.pop('artist')
    #     playlist_data = validated_data.pop('playlist')

    #     genre_instance, created = Genre.objects.get_or_create(genre_type=genre_data['genre_type'])
    #     song = Song.objects.create(**validated_data)
    # #     # Genre.objects.create(song=song, **genre_data)
    #     for album in album_data:
    #         album_instance, created = Album.objects.get_or_create(name=album['name'])
    #         song.album.add(album_instance)
    #     for artist in artist_data:
    #         artist_instance, created = Artist.objects.get_or_create(name=artist['name'])
    #         song.artist.add(artist_instance)
    #     for playlist in playlist_data:
    #         playlist_instance, created = Playlist.objects.get_or_create(name=playlist['name'])
    #         song.playlist.add(playlist_instance)
    #     # Album.objects.create(song=song, **album_data)
    # #     Artist.objects.create(song=song, **artist_data)
    # #     Playlist.objects.create(song=song, **playlist_data)

    #     return song

    # def update(self, instance, validated_data):
    #     genre_data = validated_data.pop('genre')
    #     album_data = validated_data.pop('album')
    #     artist_data = validated_data.pop('artist')
    #     playlist_data = validated_data.pop('playlist')

    #     album = (instance.album).all()
    #     album = list(album)
    #     artist = (instance.artist).all()
    #     artist = list(artist)
    #     playlist = (instance.playlist).all()
    #     playlist = list(playlist)

    #     instance.title = validated_data.get('title', instance.title)
    #     instance.duration = validated_data.get('duration', instance.duration)
    #     instance.genre = validated_data.get('genre', instance.genre)
    #     instance.plays = validated_data.get('plays', instance.plays)
    #     instance.explicit = validated_data.get('explicit', instance.explicit)
    #     instance.save()
    #     for album_data in album_data:
    #         albums = album.pop(0)
    #         # albums.id = album_data.get('id', albums.id)
    #         albums.name = album_data.get('name', albums.name)
    #         albums.release_date = album_data.get('release_date', albums.release_date)
    #         albums.save()
    #     return instance

        # for album_data in album_data:
        #     albums = album.pop(0)
        #     # albums.id = album_data.get('id', albums.id)
        #     albums.name = album_data.get('name', albums.name)
        #     albums.release_date = album_data.get('release_date', albums.release_date)
        #     albums.save()
        # return instance

        # instance.album = validated_data.get(album, instance.album)
        # # instance.title = validated_data.get('title', instance.title)
        # instance.save()

        # album_data = validated_data.get('album')

        # for album in album_data:
        #     album_id = album.get('id', None)
        #     if album_id:
        #         song_album = Album.objects.get(id=album_id, album=instance)
        #         song_album.name = album.get('name', song_album.name)
        #         song_album.release_date = album.get('release_date', song_album.release_date)
        #         song_album.save()
            # else:
            #     InvoiceItem.objects.create(account=instance, **item)

        # return instance
    #     genre_data = validated_data.pop('genre')
    #     album_data = validated_data.pop('album')
    #     artist_data = validated_data.pop('artist')
    #     playlist_data = validated_data.pop('playlist')

    #     genre_instance, updated = Genre.objects.get_or_create(genre_type=genre_data['genre_type'])
    #     song = Song.objects.update(**validated_data)
    # #     # Genre.objects.create(song=song, **genre_data)
    #     for album in album_data:
    #         album_instance, updated = Album.objects.get(name=album['name'])
    #         song.album.add(album_instance)
    #     for artist in artist_data:
    #         artist_instance, updated = Artist.objects.get(name=artist['name'])
    #         song.artist.add(artist_instance)
    #     for playlist in playlist_data:
    #         playlist_instance, updated = Playlist.objects.get(name=playlist['name'])
    #         song.playlist.add(playlist_instance)
 