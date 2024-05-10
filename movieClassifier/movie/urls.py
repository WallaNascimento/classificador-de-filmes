from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('addMovie/', views.addMovie, name='addMovie'),
path('deleteMovie/<str:pk>/', views.deleteMovie, name='deleteMovie'),
path('update/<str:pk>/', views.update, name='update'),
path('updateMovie/<str:pk>/', views.updateMovie, name='updateMovie'),
path('addGenreMovie/<str:pk>/', views.addGenreMovie, name='addGenreMovie'),
path('getMovie/<str:pk>/', views.getMovie, name='getMovie'),
path('addMovieStreaming/<str:pk>/', views.addMovieStreaming, name='addMovieStreaming'),
path('search/', views.search, name='search'),
path('addMoviePlaylist/<str:pk>/', views.addMoviePlaylist, name='addMoviePlaylist'),
path('evaluation/', views.evaluation, name='evaluation'),
path('movieWatched/<str:pk>/', views.movieWatched, name='movieWatched'),
path('like/<str:pk>/', views.like, name='like'),
path('dislike/<str:pk>/', views.dislike, name='dislike'),
    ]