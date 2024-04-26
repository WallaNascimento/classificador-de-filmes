from django.db import models

from user.models import User

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
  # date = models.DateField
      
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class GenreMovie(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + "  -  " + self.genre.name
    
class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MovieStreaming(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    platform=models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name + "  -  " + self.platform.name


class MovieWatched(models.Model):
     movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
     user=models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
         return self.user.name + "  -  " + self.movie.name

class Playlist(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + "  -  " + self.movie.name
