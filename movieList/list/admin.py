from django.contrib import admin

from .models  import Movie, Genre, GenreMovie, Platform, MovieStreaming, MovieWatched, Playlist, Evaluation 

# Register your models here.
admin.site.register(Movie)

admin.site.register(Genre)
admin.site.register(GenreMovie)
admin.site.register(Platform)
admin.site.register(MovieStreaming)


admin.site.register(MovieWatched)
admin.site.register(Playlist)
admin.site.register(Evaluation)
