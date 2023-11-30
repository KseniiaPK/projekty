import json
from filmy.models import Movie
from django.core.management.base import BaseCommand

class Command(BaseCommand):

     def handle(self,**options):
            with open('filmy/data/movies.json', encoding='utf-8') as file:
                data = json.load(file)
                for movie in data:
                    Movie.objects.update_or_create(
                        name=movie['name'],
                        year=movie['year'],
                        type=movie['type'],
                        country=movie['country'],
                        old=movie['old'],
                        genre=movie['genre'],
                        info=movie['info'],
                        photo=movie['photo'],


                )
