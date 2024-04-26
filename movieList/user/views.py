from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logining

# Create your views here.

def register(request):

    return render(request, 'register.html')

def registerUser(request):
    try:
        check_email = request.POST['femail']
        if check_email:
            return render(request, 'register.html', {'msg':'Error! Já existe usuário com este e-mail'})
    
    except User.DoesNotExist:
        name = request.POST['fname']
        email = request.POST['femail']
        password = request.POST['fpassword']

        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
    
        return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html')

def loginUser(request):
    email = request.POST['femail']
    password = request.POST['fpassword']

    user = User.objects.get(email = email) 
    username=user.username
    user = authenticate(username=username, password = password)
    if user is not None:
        logining(request, user)
        return redirect('http://127.0.0.1:8000/')
        #return render(request, 'index.html')
    
    
def logout(request):
    request.session.flush()
    return redirect('http://127.0.0.1:8000/')