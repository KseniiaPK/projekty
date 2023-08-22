from django.core.management.base import BaseCommand
from eshop.models import Kategorie

class Command(BaseCommand):
    def handle(self, *args, **options):

        print('Command is called')
        path = 'eshop/management/data/kategorie.txt'
        with open(path, encoding='UTF-8') as soubor:
            nad_kategorie = None
            for radek in soubor:
                radek = radek.strip()
                if radek.endswith(':'):
                    print('vytvorena kategorie', radek)
                    nad_kategorie,_ = Kategorie.objects.update_or_create(nazev=radek[:-1])
                else:
                    print('vytvorena kategorie', radek, nad_kategorie)
                    Kategorie.objects.update_or_create(nazev=radek,nadkategorie=nad_kategorie)

                print(radek.strip())