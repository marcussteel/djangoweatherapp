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

  
