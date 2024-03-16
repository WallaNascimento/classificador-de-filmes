from django.shortcuts import render, redirect

from django.http import HttpResponse
from list.models import Movie

# Create your views here.

def index(request):
    movie = Movie.objects.all()
    context = {'movie':movie}
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
