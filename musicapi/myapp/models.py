from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=500)
    bio = models.TextField(max_length=1000)
    image = models.URLField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=500)
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_type = models.CharField(max_length=500)

    def __str__(self):
        return self.genre_type  

class Song(models.Model):
    title = models.CharField(max_length=500)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=3)
    album = models.ManyToManyField(Album)
    artist = models.ManyToManyField(Artist)
    plays = models.IntegerField(default=0)
    explicit = models.BooleanField(default=False)
    playlist = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.title 

# class ReadSong(model.Model):
#     title = models.CharField(max_length=500)
#     duration = models.DecimalField(max_digits=4, decimal_places=2)
#     genre = models.ForeignKey(Genre, on_delete=models.PROTECT, default=3)
#     album = models.ManyToManyField(Album)
#     artist = models.ManyToManyField(Artist)
#     plays = models.IntegerField(default=0)
#     explicit = models.BooleanField(default=False)
#     playlist = models.ManyToManyField(Playlist)

#     def __str__(self):
#         return self.title 