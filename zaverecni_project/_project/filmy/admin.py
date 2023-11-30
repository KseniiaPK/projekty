from django.contrib import admin
from .models import Movie, Type, Genre, Country

admin.site.register(Movie)
admin.site.register(Type)
admin.site.register(Genre)
admin.site.register(Country)

# Register your models here.
