from django.urls import path
from . import views

urlpatterns = [
#path('', views.index, name='index'),
path('register/', views.register, name='register'),
path('registerUser/', views.registerUser, name='registerUser'),
path('login/', views.login, name='login'),
path('loginUser/', views.loginUser, name='loginUser'),
path('logout/', views.logout, name='logout'),
path('profile/', views.profile, name='profile'),
path('follow/<str:pk>/', views.follow, name='follow'),
path('getMovieWatched_userFollowing/', views.getMovieWatched_userFollowing, name='getMovieWatched_userFollowing'),
path('getMyPlaylist/', views.getMyPlaylist, name='getMyPlaylist'),
path('getMyMovieWatched/', views.getMyMovieWatched, name='getMyMovieWatched'),
    
    ]