from django.urls import path, include
from .views import search


urlpatterns = [
    path('home', search, name='home')

    
]