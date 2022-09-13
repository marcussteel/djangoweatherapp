import imp
from urllib import response
from django.shortcuts import render
from decouple import config
import requests

def index(request):
    API_KEY=config('API_KEY')
    city = "Yozgat"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    content= response.json()
    return render(request, 'weatherapp/index.html')




