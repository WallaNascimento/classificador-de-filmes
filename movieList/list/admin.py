from django.contrib import admin

from .models  import Movie, Genre, GenreMovie, Platform, MovieStreaming 

# Register your models here.
admin.site.register(Movie)

admin.site.register(Genre)
admin.site.register(GenreMovie)
admin.site.register(Platform)
admin.site.register(MovieStreaming)

