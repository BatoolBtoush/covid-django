from django.shortcuts import render
import requests
from .models import CountryData

# from django.contrib import messages
from django.views.generic import ListView, DeleteView
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404





def home(request):
    first_response = requests.get("https://api.covid19api.com/world/total").json()
    # second_response = requests.get('https://api.covid19api.com/country/south-africa/status/confirmed?from=2020-09-06T00:00:00Z&to=2020-09-11T00:00:00Z').json()
    second_response = requests.get("https://api.covid19api.com/summary").json()

    my_list = []
    req_js = []
    dates_list = []
    cases_list = []
    bigger_list = zip(dates_list, cases_list)

    for i in range(0, len(second_response["Countries"])):
        my_list.append(second_response["Countries"][i]["Country"])

    if request.method == "POST":
        selected_country = request.POST["selected_country"]
        start_date = request.POST["start_date"]
        end_date = request.POST["end_date"]
        request_handler = requests.get(
            f"https://api.covid19api.com/country/{selected_country}/status/confirmed?from={start_date}T00:00:00Z&to={end_date}T00:00:00Z"
        )
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
                cases = req_js[0][i]["Cases"]
                dates = req_js[0][i]["Date"]
                cases_list.append(cases)
                dates_list.append(dates)
                # new_dict = {case : date for i in req_js[0]}
                # return new_dict
                # print(cases_and_date)
        else:
            req_js.append(1)

    context = {
        "first_response": first_response,
        "my_list": my_list,
        "req_js": req_js,
        # 'new_dict': new_dict.items(),
        # 'cases_list': cases_list,
        # 'dates_list': dates_list
        "bigger_list": bigger_list,
    }

    return render(request, "home.html", context)


def all_countries(request):
    first_response = requests.get("https://api.covid19api.com/summary").json()
    results = len(first_response["Countries"])
    my_new_list = []
    data_list = []

    for i in range(0, results):
        my_new_list.append(first_response["Countries"][i])

    if request.method == "POST":
        if request.POST.get("country") and request.POST.get("date"):
            added_record = CountryData()
            added_record.country = request.POST.get("country")
            # 2022-12-19T08:53:48.179Z
            added_record.date = datetime.datetime.strptime(
                request.POST.get("date"), "%Y-%m-%dT%I:%M:%S.%fZ"
            )
            added_record.save()
            return render(request, "allcountries.html")
        else:
            return render(request, "allcountries.html" )

    context = {"my_new_list": my_new_list}
    return render(request, "allcountries.html", context)


class MyRecords(ListView):
    template_name = "myrecords.html"
    model = CountryData
    context_object_name = "records_list"


# class DeleteMyRecord(DeleteView):
#     template_name = "deleterecord.html"
#     model = CountryData
#     success_url = "/"


def delete(request, id):
    note = get_object_or_404(CountryData, pk=id).delete()
    success_url = "/myrecords"
    return HttpResponseRedirect(success_url)