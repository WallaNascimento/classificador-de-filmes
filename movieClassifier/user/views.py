from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User, Follow 
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login as logining
from movie.models import Movie, Genre, GenreMovie, Platform, MovieStreaming, Playlist, Evaluation, MovieWatched, Like, Dislike
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    return render(request, 'register.html')

def registerUser(request):
    try:
        email = request.POST['femail']
        check_email = User.objects.get(email=email)
        if check_email:
            return render(request, 'register.html', {'msg':'Error! Já existe usuário com este e-mail'})

    except User.DoesNotExist:
        name = request.POST['fname']
        email = request.POST['femail']
        number = request.POST['fnumber']
        password = request.POST['fpassword']

    #newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser = User(
        username = name,
        email = email,
        number = number,
        password = password,
    )
        newUser.set_password(password)
        
        newUser.save()
    
        return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html')

def loginUser(request):
    email = request.POST['femail']
    password = request.POST['fpassword']

    #username = User.objects.get(email = email).email
    user = authenticate(request, email=email, password = password)
    #if user.check_password(password) and user.user_can_authenticate(user):  
    if user is not None:
         logining(request, user)
         return redirect('http://127.0.0.1:8000/')
    else:
        return HttpResponse(user)
        #return render(request, 'login.html', {'msg': "Error! Usuário não encontrado."})

    
    
def logout(request):
    request.session.flush()
    return redirect('http://127.0.0.1:8000/')

@login_required(login_url="login")
def profile(request):
    userId = request.user.id
    user = User.objects.get(id=userId)
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)

@login_required(login_url="login")
def follow(request, pk):
    userId = request.user.id
    user = User.objects.get(id=userId)
    
    userFollowing = User.objects.get(id=pk)
    if user != userFollowing:
        try:
            following = user.users.following.all()
            if userFollowing in following:      
                user.users.following.remove(userFollowing)
            else:
                user.users.following.add(userFollowing)
        except User.users.RelatedObjectDoesNotExist:
            newUser = Follow(
          user =user
      )
             
            newUser.save()
            user.users.following.add(userFollowing)
    
        return JsonResponse(status=200, data={'status':'false','message':"Tudo certo"})
    else:
        return JsonResponse(status=200, data={'status':'false','message':"Tudo certo"})
    

@login_required(login_url="login")
def getMyPlaylist(request):
    results = Playlist.objects.filter(user=request.user)
    return render(request, 'profile.html', {'results':results})
    
@login_required(login_url="login")
def getMyMovieWatched(request):
    results = MovieWatched.objects.filter(user=request.user)
    return render(request, 'profile.html', {'results':results})
        
    
@login_required(login_url="login")
def getMovieWatched_userFollowing(request):
    userFollow = Follow.objects.get(user=request.user)
    users_followed = userFollow.following.all() 
    results = MovieWatched.objects.filter(user__in=users_followed) #.select_related('movies')
    return render(request, 'profile.html', {'results':results})
    