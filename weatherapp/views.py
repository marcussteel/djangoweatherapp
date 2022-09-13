import imp
from pyexpat.errors import messages
from urllib import response
from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages
from .models import City

def index(request):
    API_KEY=config('API_KEY')
    city = "yozgat"
    u_city = request.POST.get("name")


    if u_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        print(response.ok)
        if response.ok:
            content = response.json()
            r_city = content["name"]
            if City.objects.filter(name=r_city):
                messages.warning(request,"City already exist")
            else:
                City.objects.create(name=r_city)

            
            context = {
                "city": content["name"],
                "temp": content["main"]["temp"],
                "desc": content["weather"][0]["description"],
                "icon": content["weather"][0]["icon"]
            }
            return render(request, 'weatherapp/index.html', context)
        else:
            messages.warning(request,"no city")




    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    content= response.json()
    # pprint(content)
    # pprint(content["name"])
    # pprint(content["main"]["temp"])
    # pprint(content["weather"][0]["description"])
    # pprint(content["weather"][0]["icon"])
    context={
        "city" : content["name"],
        "temp" : content["main"]["temp"],
        "desc" : content["weather"][0]["description"],
        "icon" : content["weather"][0]["icon"]
    }
    return render(request, 'weatherapp/index.html',context)


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
