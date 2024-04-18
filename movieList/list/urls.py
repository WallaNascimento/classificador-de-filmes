from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('addMovie/', views.addMovie, name='addMovie'),
path('deleteMovie/<str:pk>/', views.deleteMovie, name='deleteMovie'),
path('update/<str:pk>/', views.update, name='update'),
path('updateMovie/<str:pk>/', views.updateMovie, name='updateMovie'),
path('addGenre/', views.addGenre, name='addGenre'),
path('addGenreMovie/<str:pk>/', views.addGenreMovie, name='addGenreMovie'),
path('getMovie/<str:pk>/', views.getMovie, name='getMovie'),
    ]