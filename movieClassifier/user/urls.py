from django.urls import path
from . import views

urlpatterns = [
#path('', views.index, name='index'),
path('register/', views.register, name='register'),
path('registerUser/', views.registerUser, name='registerUser'),
path('login/', views.login, name='login'),
path('loginUser/', views.loginUser, name='loginUser'),
path('logout/', views.logout, name='logout'),
path('follow/<str:pk>/', views.follow, name='follow'),
#path('deleteMovie/<str:pk>/', views.deleteMovie, name='deleteMovie'),
#path('update/<str:pk>/', views.update, name='update'),
#path('updateMovie/<str:pk>/', views.updateMovie, name='updateMovie'),
    ]