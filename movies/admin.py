from django.contrib import admin

from movies.models import Movie, Director, Genre, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'footage']
    list_display_links = ['id', 'title']
    search_fields = ["=id", "title", "director__name"]
    list_filter = ['year', "genres"]
    list_editable = ['year', 'footage']

admin.site.register(Movie, MovieAdmin)


class DirectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Director, DirectorAdmin)


class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)


class ActorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actor, ActorAdmin)
