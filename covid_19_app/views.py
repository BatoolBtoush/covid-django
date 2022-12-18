from django.shortcuts import render
import requests
# from django.views.generic import ListView


def home(request):
    first_response = requests.get('https://api.covid19api.com/world/total').json()
    # second_response = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-09-06T00:00:00Z&to=2020-09-11T00:00:00Z').json()
    second_response = requests.get('https://api.covid19api.com/summary').json()

    my_list = []
    req_js = []
    dates_list = []
    cases_list = []
    bigger_list =zip(dates_list, cases_list)


    for i in range(0, len(second_response['Countries'])):
        my_list.append(second_response['Countries'][i]['Slug'])

    if request.method =='POST':
        selected_country = request.POST['selected_country']
        start_date= request.POST['start_date']
        end_date= request.POST['end_date']
        request_handler = requests.get(f"https://api.covid19api.com/country/{selected_country}/status/confirmed?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z")
        if request_handler.status_code == 200:
            request_json = request_handler.json()
            # print('request_json', request_json)
            # print('selected_country',selected_country)
            req_js.append(request_json)
            # print(len(req_js[0]))
            for i in range(len(req_js[0])):
                
                # dicts = req_js[0][i]
                # # print(dicts)
                # # cases_and_date = req_js[0][i]
                # case = dicts.get("Cases")
                # date = dicts.get("Date")
                cases = req_js[0][i]['Cases']
                dates = req_js[0][i]['Date']
                cases_list.append(cases)
                dates_list.append(dates)
                # new_dict = {case : date for i in req_js[0]}
                # return new_dict
                # print(cases_and_date)
        else:
            req_js.append(1)

    context = {
        'first_response':first_response, 
        'my_list': my_list,
        'req_js': req_js,
        # 'new_dict': new_dict.items(),
        # 'cases_list': cases_list,
        # 'dates_list': dates_list
        'bigger_list': bigger_list

    }
    
    return render(request, 'home.html', context)




def all_countries(request):
    first_response = requests.get('https://api.covid19api.com/summary').json()
    results =  len(first_response['Countries'])
    my_new_list = []


    for i in range(0, results):
        my_new_list.append(first_response['Countries'][i])
  
    context = {'my_new_list': my_new_list}
    return render(request, 'allcountries.html', context)