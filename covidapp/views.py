import requests
from django.shortcuts import render


# Create your views here.
def index(request):
    data = True
    response = None
    global_summary = None
    countries = None
    while data:
        try:
            url = "https://api.covid19api.com/summary"
            response = requests.request("GET", url).json()
            global_summary = response['Global']
            countries = response['Countries']
            data = False
        except:
            data = True
    context = {
        'global_summary': global_summary,
        'countries': countries,
    }
    return render(request, 'covidapp/index.html', context)
