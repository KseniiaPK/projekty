from eshop.models import Kategorie, Znacka


def kategorie_context(request):
    kategorie = Kategorie.objects.select_related('nadkategorie')

    return {
        'KATEGORIE': kategorie,
    }
def znacka_context(request):
    znacka = Znacka.objects.all()
    return{
        'ZNACKA': znacka
    }