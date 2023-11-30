from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name ="homepage"),
    path("allmovies/",views.movie_list,name="allmovies"),
    path("films/",views.films_list,name="films"),
    path("series/",views.series_list,name="series"),
    path("cartoons/",views.cartoons_list,name="cartoons"),
    path("types/",views.types_list,name="types"),
    path("genres/",views.genres_list,name="genres"),
    path("movie_detail/<str:name>",views.movie_detail,name="movie_detail"),
    path("countries/",views.countries_list,name="countries"),
    path("movies_by_genre/<str:genre_name>", views.movies_by_genre,name="movies_by_genre"),
    path("movies_by_country/<str:country_name>", views.movies_by_country,name="movies_by_country"),


]