from django.shortcuts import render
from . forms import SearchForm
from django.contrib import messages
import requests
import datetime
import os

# Create your views here.

def index_view(request):
    context = {}
    if request.method == "POST":
        context['form'] = SearchForm(request.POST)
        if context['form'].is_valid():
            city = context['form'].cleaned_data["city_search"]

            api_key = os.environ.get('OPEN_WEATHER_API_KEY')

            api_call = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

            response = requests.get(api_call.format(city, api_key)).json()

            if response['cod'] == "404":
                messages.error(request, "City name entered does not exist.")
            else:
                context['name'] = response['name']
                context['date'] = datetime.datetime.now().strftime("%a %H:%M%p")
                context['temperature'] = response['main']['temp']
                context['description'] = response['weather'][0]['description']
                context['icon'] = response['weather'][0]['icon']
                context['country'] = response['sys']['country']
    else:
        context['form'] = SearchForm()

    return render(request, "index/index.html", context)
    