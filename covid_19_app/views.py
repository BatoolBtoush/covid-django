from django.shortcuts import render
import requests
# from django.views.generic import ListView


def home(request):
    first_response = requests.get('https://api.covid19api.com/world/total').json()
    # second_response = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-09-06T00:00:00Z&to=2020-09-11T00:00:00Z').json()
    second_response = requests.get('https://api.covid19api.com/summary').json()

    my_list = []
    for i in range(0, len(second_response['Countries'])):
        my_list.append(second_response['Countries'][i]['Country'])


    if request.method=='POST':
        selected_country = request.POST['selected_country']
        print('here', selected_country)


    
    return render(request, 'home.html', {'first_response':first_response, 'my_list': my_list})




def country(request):
    response = requests.get('https://api.covid19api.com/summary').json()
    results =  len(response['Countries'])
    # print(results)
    # print(response['Countries'])
    # print(response['Countries'][0]['Country'])
    my_new_list = []
    for i in range(0, results):
        my_new_list.append(response['Countries'][i])
    context = {'my_new_list': my_new_list}
    return render(request, 'allcountries.html', context)
