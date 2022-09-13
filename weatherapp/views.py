import imp
from urllib import response
from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

def index(request):
    API_KEY=config('API_KEY')
    city = "Yozgat"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    content= response.json()
    # pprint(content)
    pprint(content["name"])
    pprint(content["main"]["temp"])
    pprint(content["weather"][0]["description"])
    pprint(content["weather"][0]["icon"])

    return render(request, 'weatherapp/index.html')


{'base': 'stations',
 'clouds': {'all': 29},
 'cod': 200,
 'coord': {'lat': 39.5833, 'lon': 35.3333},
 'dt': 1663090364,
 'id': 296560,
 'main': {'feels_like': 288.12,
          'grnd_level': 883,
          'humidity': 56,
          'pressure': 1008,
          'sea_level': 1008,
          'temp': 289.02,
          'temp_max': 289.02,
          'temp_min': 289.02},
 'name': 'Yozgat Province',
 'sys': {'country': 'TR', 'sunrise': 1663039064, 'sunset': 1663084316},
 'timezone': 10800,
 'visibility': 10000,
 'weather': [{'description': 'scattered clouds',
              'icon': '03n',
              'id': 802,
              'main': 'Clouds'}],
 'wind': {'deg': 48, 'gust': 1.92, 'speed': 1.16}}
