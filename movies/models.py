from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text="in minutes")
    photo = models.ImageField(upload_to="photos/movies", blank=True, null=True)
    director = models.ForeignKey("Director", blank=True, null=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField("Actor", blank=True, null=True)
    genres = models.ManyToManyField("Genre", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def genres_display(self):
        return ", ".join([genre.name for genre in self.genres.all()])
    
class Director(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/directors", blank=True, null=True)
    birthyear = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/actors", blank=True, null=True)
    birthyear = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name