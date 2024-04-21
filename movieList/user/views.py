from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.http import HttpResponse
from user.models import User 

# Create your views here.

def register(request):

    return render(request, 'register.html')

def registerUser(request):
    name = request.POST['fname']
    email = request.POST['femail']
    password = request.POST['fpassword']
    newUser = User(
        name = name,
        email = email,
        password = password,
    )
    newUser.save()
    
    return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html')

def loginUser(request):
    email = request.POST['femail']
    password = request.POST['fpassword']
    
    return render(request, 'index.html')
def logout(request):
    request.session.flush()
    return redirect('http://127.0.0.1:8000/')