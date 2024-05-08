from django.db import models

from user.models import User
import datetime 
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    description = models.CharField(max_length=500)
    
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
         return self.user.username + "  -  " + self.movie.name

class Playlist(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + "  -  " + self.movie.name

class Evaluation(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.IntegerField()
    comment = models.CharField(max_length=100)
    publication = models.DateTimeField(auto_now_add=True)
       
    def __str__(self):
        return str(self.user.username) + " - " + str(self.movie.name) + " - " + str(self.comment) + " - " + str(self.classification) + " - " + str(self.publication)
    
class Like(models.Model):
    like = models.IntegerField(default=0)
    deslike = models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation=models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.like) + "-" + str(self.deslike)
