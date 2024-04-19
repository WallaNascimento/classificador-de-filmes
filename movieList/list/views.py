from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.http import HttpResponse
from list.models import Movie, Genre, GenreMovie, Platform, MovieStreaming

# Create your views here.

def index(request):
    movie = Movie.objects.all()
    genre = Genre.objects.all()
    genremovie = GenreMovie.objects.all()
    
    context = {'movie':movie, 
        'genre':genre,
        'genremovie':genremovie,
               }
    return render(request, 'index.html', context)
    
def addMovie(request):
    name = request.POST['fname']
    duration = request.POST['fduration']
    newMovie = Movie(
        name = name,
        duration = duration,
    )
    newMovie.save()
    return redirect('http://127.0.0.1:8000/')
        
def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('http://127.0.0.1:8000/')

def update(request, pk):
    movie = Movie.objects.get(id=pk)
        
    return render(request, 'updateMovie.html',{"Movie":movie})

def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    
    name = request.POST['fname']
    duration = request.POST['fduration']
    movie.name = name
    movie.duration = duration
    
    movie.save()
    return redirect('http://127.0.0.1:8000/')


def getMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    list_genre_movie = GenreMovie.objects.filter(movie__id=pk)
    genres = Genre.objects.all()
    list_streaming_movie = MovieStreaming.objects.filter(movie__id=pk)
    platforms = Platform.objects.all()
    
    context = {
        'genres': genres,
        'movie': movie,
        'list_genre_movie':list_genre_movie,
        'platforms':platforms,
        'list_streaming_movie':list_streaming_movie,
        }
    return render(request, 'showGenreMovie.html', context)


def addGenreMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    genreId = request.POST['genre']
    genre = Genre.objects.get(id=genreId)
    
    newGenreMovie = GenreMovie (
        movie = movie,
        genre = genre,
    )
    newGenreMovie.save()
    
    return redirect('http://127.0.0.1:8000/')
    
def addMovieStreaming(request, pk):
    movie = Movie.objects.get(id=pk)
    platformId = request.POST['platform']
    platform = Platform.objects.get(id=platformId)
    
    newMovieStreaming = MovieStreaming (
        movie = movie,
        platform = platform,
    )
    newMovieStreaming.save()
    
    return redirect('http://127.0.0.1:8000/')
  
