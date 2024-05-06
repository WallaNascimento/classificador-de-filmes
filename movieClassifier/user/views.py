from django.shortcuts import render, redirect


from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User 
#from django.contrib.auth.models import User
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
        name = name,
        email = email,
        number = number,
        password = password,
    )
        newUser.save()
    
        return render(request, 'index.html') 

def login(request):
    return render(request, 'login.html')

def loginUser(request):
    email = request.POST['femail']
    password = request.POST['fpassword']

    username = User.objects.get(email = email.lower()).name
    #username=user.name
    user = authenticate(request, username=username, password = password)
   
    if user is not None:
         logining(request, user)
         return redirect('http://127.0.0.1:8000/')
    else:
        return HttpResponse(username)
        #return render(request, 'login.html', {'msg': "Error! Usuário não encontrado."})

    
    
def logout(request):
    request.session.flush()
    return redirect('http://127.0.0.1:8000/')

# def follow(request, pk):
#     userId = request.user.id
#     user = User.objects.get(id=userId)
#     userFollow = User.objects.get(id=pk)
#     #newFollow = Follow(
#         user = user,
#         userFollow = userFollow,
#     )
#     newFollow.save()
        
#     return redirect('http://127.0.0.1:8000/')
 
