from django.urls import path, include
from .views import home, country


urlpatterns = [
    path('home', home, name='home'),
    path('allcountries', country, name='all_countries'),

   
]