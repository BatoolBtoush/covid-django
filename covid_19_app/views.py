from django.shortcuts import render, HttpResponse
import requests

# Create your views here.

# def home(request):
#     response = requests.get('https://api.covid19api.com/world/total').json()
#     context = {'response':response}
#     return render(request, 'home.html', context)



def search(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    my_list = []
    for i in range(0, len(response)):
        my_list.append(response[i]['Country'])
    context = {'my_list': my_list}
    return render(request, 'home.html', context)



# class HomePage(TemplateView):
#     template_name = 'home.html'

#     def home(self, request):
#         response = requests.get('https://api.covid19api.com/world/total').json()
#         print('res',response.data)
#         return render(request, 'home.html', {'response': response})


#     def other(self, request):
#         reoth = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-09-06T00:00:00Z&to=2020-09-11T00:00:00Z').json()
#         return render(request, 'home.html', {'response': reoth})
