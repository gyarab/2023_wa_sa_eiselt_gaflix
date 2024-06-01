from django.shortcuts import render
from movies.models import Movie

def movies(request):
    context = {
        "movies": Movie.objects.all().order_by('title')
    }

    return render(request, "movies/movies.html", context)


def movie(request, id):
    movie = Movie.objects.get(id=id)

    context = {
        "movie": movie,
    }

    return render(request, "movies/movie.html", context)