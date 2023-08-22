
from django.urls import path
from eshop.views import (
    index,
    kategorie_list,
    kategorie_detail,
    znacka,
    produkt_detail,
    produkt_list,
)


app_name = 'eshop'

urlpatterns = [
    path('', index, name='index'),
    path('kategorie/', kategorie_list, name='kategorie_list'),
    path('produkty/', produkt_list, name='produkt_list'),
    path('<slug:slug>/', kategorie_detail, name='kategorie_detail'),
    path('znacka/<slug:slug>/', znacka, name='znacka'),
    path('p/<slug:slug>/<int:pk>/', produkt_detail, name='produkt_detail'),
]