from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('addMovie/', views.addMovie, name='addMovie'),
path('deleteMovie/<str:pk>/', views.deleteMovie, name='deleteMovie'),
    ]