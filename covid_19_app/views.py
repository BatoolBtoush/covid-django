from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

def home(request):
    response = requests.get('https://api.covid19api.com/world/total').json()
    return render(request, 'home.html', {'response':response})
