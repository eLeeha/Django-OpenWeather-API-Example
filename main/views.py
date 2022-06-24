from multiprocessing import context
from django.shortcuts import render
import requests
from .forms import WetterForm
from datetime import datetime
from django.conf import settings

def wetter(request):
  if request.method == 'POST':
    form = WetterForm(request.POST)
    if form.is_valid(): 
      city = form.cleaned_data['city_input']
    else:
      city = settings.DEFAULT_CITY
  else:
    ### Default city
    city = settings.DEFAULT_CITY

  url = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format(city, settings.API_KEY)
  city_weather = requests.get(url).json() #request the API data and convert the JSON to Python data types

  if city_weather['cod'] == 200:
    weather = {
          'city' : city_weather['name'],
          'country' : city_weather['sys']['country'],
          'temperature' : city_weather['main']['temp'],
          'temparature_feel' : city_weather['main']['feels_like'],
          'temparatur_max' : city_weather['main']['temp_max'],
          'humidity' : city_weather['main']['humidity'],
          'sunrise' : datetime.fromtimestamp(city_weather['sys']['sunrise']).strftime("%H:%M:%S"),
          'sunset' : datetime.fromtimestamp(city_weather['sys']['sunset']).strftime("%H:%M:%S"),
          'description' : city_weather['weather'][0]['description'],
          'icon' : city_weather['weather'][0]['icon'],
          'error' : None
      }
  else:
    weather = {
          'city' : None,
          'country' : None,
          'temperature' : None,
          'temparature_feel' : None,
          'description' : None,
          'icon' : None,
          'temparatur_max' : None,
          'humidity' : None,
          'sunrise' : None,
          'sunset' : None,
          'error' : city_weather['message']
      }
  context = {'weather' : weather}
  
  return render(request, 'main/wetter.html', context)
