from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User, Follow 
#from django.contrib.auth.models import User
#acima comentar
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login as logining

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

def follow(request, pk):
    userId = request.user.id
    user = User.objects.get(id=userId)
    
    userFollowing = User.objects.get(id=pk)
    
    
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


                       
        
    return redirect('http://127.0.0.1:8000/')
 
