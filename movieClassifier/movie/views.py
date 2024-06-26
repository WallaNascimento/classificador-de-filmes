from django.shortcuts import render, redirect

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from movie.models import Movie, Genre, GenreMovie, Platform, MovieStreaming, Playlist, Evaluation, MovieWatched, Like, Dislike
from user.models import User, Follow

#from django.contrib.auth.models import User

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
    description = request.POST['fdescription']
    
    newMovie = Movie(
        name = name,
        duration = duration,
        description = description,
    )
    newMovie.save()
    return redirect('http://127.0.0.1:8000/')
        
def deleteMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('http://127.0.0.1:8000/')
    #return JsonResponse(status=200, data={'status':'false','message':"Tudo certo"})


def update(request, pk):
    movie = Movie.objects.get(id=pk)
#     newMovie = {
# "name": movie.name,
#             "duration": movie.duration,
#             "description": movie.description, 
# }
#     return JsonResponse(newMovie)

    movie = Movie.objects.get(id=pk)
        
    return render(request, 'updateMovie.html',{"Movie":movie})

def updateMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    
    name = request.POST['fname']
    duration = request.POST['fduration']
    description = request.POST['fdescription']
    
    movie.name = name
    movie.duration = duration
    movie.description = description
    
    movie.save()
    return redirect('http://127.0.0.1:8000/')


def getMovie(request, pk):
    movie = Movie.objects.get(id=pk)
    list_genre_movie = GenreMovie.objects.filter(movie__id=pk)
    genres = Genre.objects.all()
    list_streaming_movie = MovieStreaming.objects.filter(movie__id=pk)
    platforms = Platform.objects.all()
    evaluation = Evaluation.objects.filter(movie__id=pk)

    like = Like.objects.all()
        
    follow = Follow.objects.all()
            
    context = {
        'genres': genres,
        'movie': movie,
        'list_genre_movie':list_genre_movie,
        'platforms':platforms,
        'list_streaming_movie':list_streaming_movie,
        'evaluation': evaluation,
        'like':like,
        'follow':follow,
        }
    return render(request, 'showMovie.html', context)

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
  
def search(request):
    name = request.POST['search']
    search = Movie.objects.filter(name=name)
    
    return render(request, 'index.html', {'search':search})

def addMoviePlaylist(request, pk):
    movie = Movie.objects.get(id=pk)
    userId = request.user.id
    user = User.objects.get(id=userId)
    
    newMoviePlaylist = Playlist (
        movie = movie,
        user = user,
    )
    newMoviePlaylist.save()
    
    return redirect('http://127.0.0.1:8000/')

def movieWatched(request, pk):
    movie = Movie.objects.get(id=pk)
    userId = request.user.id
    user = User.objects.get(id=userId)
    
    newMovieWatched = MovieWatched (
        movie = movie,
        user = user,
    )
    newMovieWatched.save()
    
    return redirect('http://127.0.0.1:8000/')


def evaluation(request):
    userId = request.user.id
    movieId = request.POST['idMovie']
    movie = Movie.objects.get(id=movieId)
    user = User.objects.get(id=userId)
    classification = request.POST['cla']
    comment = request.POST['fcomment']
    newEvaluation = Evaluation(
        movie = movie,
        user = user,
        classification = classification,
        comment = comment,
    )
    newEvaluation.save()
    
    return redirect('http://127.0.0.1:8000/')
#Função de like, fazer lógica para create quando verificado avaliação==None
def like(request, pk):
    userId = request.user.id
    user = User.objects.get(id=userId)
    evaluation = Evaluation.objects.get(id=pk)
    try:
        evaluation.likes.users.add(user)
    except Evaluation.likes.RelatedObjectDoesNotExist:# as identifier:
        Like.objects.create(
            evaluation = evaluation
        )
        evaluation.likes.users.add(user)
         
    return redirect('http://127.0.0.1:8000/')

#Função de dislike, fazer lógica para create quando verificado avaliação==None
def dislike(request, pk):
    userId = request.user.id
    user = User.objects.get(id=userId)
    evaluation = Evaluation.objects.get(id=pk)
    try:
        evaluation.dislikes.users.add(user)
    except Evaluation.dislikes.RelatedObjectDoesNotExist:# as identifier:
        Dislike.objects.create(
            evaluation = evaluation
        )
        evaluation.dislikes.users.add(user)
       
    return HttpResponseRedirect('http://127.0.0.1:8000/')
    #return redirect('http://127.0.0.1:8000/')

