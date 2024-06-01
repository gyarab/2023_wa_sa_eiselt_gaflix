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
    list_display = ['id', 'name', 'birthyear']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'birthyear']
    list_editable = ['birthyear']

admin.site.register(Director, DirectorAdmin)
    


class GenreAdmin(admin.ModelAdmin):
     list_display = ['id', 'name']
     list_display_links = ['id', 'name']

admin.site.register(Genre, GenreAdmin)



class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthyear']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'birthyear']
    list_editable = ['birthyear']

admin.site.register(Actor, ActorAdmin)
