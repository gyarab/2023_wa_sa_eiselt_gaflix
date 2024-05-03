from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null=True)
    footage = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmys'

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_picture = models.ImageField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directors'

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
