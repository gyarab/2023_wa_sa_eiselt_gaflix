from django.contrib import admin

from movies.models import Movie, Director, Genre, Actor

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
