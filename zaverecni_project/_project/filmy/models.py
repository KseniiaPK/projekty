from django.db import models


class Type(models.Model):
    name_type = models.CharField(max_length=100)

class Genre(models.Model):
    name_genre = models.CharField(max_length=100)

class Country(models.Model):
    name_country = models.CharField(max_length=100)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    old = models.CharField(max_length=3)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    info = models.TextField()
    photo = models.ImageField(upload_to='movie_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


