from django.urls import path, include
from .views import home, all_countries


urlpatterns = [
    path('', home, name='home'),
    path('allcountries', all_countries, name='all_countries'),


   
]