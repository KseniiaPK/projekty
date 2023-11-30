from django.shortcuts import render
from .models import Movie, Type, Genre, Country
from django.http import JsonResponse


def movie_json(request):
    movies = Movie.objects.all()
    data=[]
    for movie in movies:
        data.append({
            'name': movie.name,
            'year': movie.year,
            'type': movie.type,
            'country': movie.country,
            'old': movie.old,
            'genre': movie.genre,
            'info': movie.info,
        })

    return JsonResponse(data, safe=False)



def movie_list(request ):
    object_list = Movie.objects.all()
    return render(request, 'allmovies.html', context={'object_list': object_list})

def index(request):
    return render(request, "index.html")

def films_list(request):
    films = Movie.objects.filter(type__name_type="film")
    return render(request, "films.html", {"films": films})

def series_list(request):
    series = Movie.objects.filter(type__name_type="serie")
    return render(request, "series.html", {"series": series})

def cartoons_list(request):
    cartoons = Movie.objects.filter(type__name_type="cartoon")
    return render(request, "cartoons.html", {"cartoons": cartoons})

def types_list(request):
    types_name = Type.objects.all()
    return render(request, "types.html", {"types": types_name})

def genres_list(request):
    genres_name = Genre.objects.all()
    return render(request, "genres.html", {"genres": genres_name})

def countries_list(request):
    countries_name = Country.objects.all()
    return render(request, "countries.html", {"countries": countries_name})

def movie_detail(request, name):
    movie = Movie.objects.get(name=name)
    return render(request, 'movie_detail.html', context={'movie': movie})

def movies_by_genre(request, genre_name):
    movies = Movie.objects.filter(genre__name_genre=genre_name)
    return render(request, "movies_by_genre.html", {"movies": movies, "genre_name": genre_name})

def movies_by_country(request, country_name):
    movies_country = Movie.objects.filter(country__name_country=country_name)
    return render(request, "movies_by_country.html", {"movies_country": movies_country, "country_name": country_name})