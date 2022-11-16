from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000)
    image = models.URLField()

class Album(models.Model):
    name = models.CharField(max_length=500)
    release_date = models.DateField()

class Playlist(models.Model):
    name = models.CharField(max_length=500)

class Genre(models.Model):
    genre_type = models.CharField(max_length=500)  

class Song(models.Model):
    title = models.CharField(max_length=500)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    album = models.ManyToManyField(Album)
    artist = models.ManyToManyField(Artist)
    plays = models.IntegerField(default=0)
    explicit = models.BooleanField(default=False)
    playlist = models.ManyToManyField(Playlist)