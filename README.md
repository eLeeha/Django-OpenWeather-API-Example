# Django OpenWeather API Example

![Python](https://img.shields.io/pypi/pyversions/Django)
![Django](https://img.shields.io/badge/django-4.0-green)

Coding web app that uses Django web framework and the OpenWaether API to retrieve weather data from a city.

A wrapper for Openweathermap One Call Api v3 -> [Link](https://openweathermap.org/api/one-call-3).

### Attention!

I am not owner or maintainer of the API (https://openweathermap.org/api). This is only a wrapper for it.
You need to get an api-key from their site to use the api.

## Requirement

You need a working environment with python <= 3.0 (recommanded Python 3.9.6)

## Installation

cd to development directory \
mkvirtualenv wetter-django \
mkdir wetter-django \
clone repository to new directory \
pip install -r requirements.txt \
Update settings.py with your email API information \
API_KEY = "XXX" 

python manage.py makemigrations \
python manage.py migrate \
python manage.py runserver \
https://localhost:8000 

## License

Django OpenWeather API Example
Copyright (C) 2022 eLeeha. GPL-3.0 license.

Django OpenWeather API Example includes several third-party Open-Source libraries, which are licensed under their
own respective Open-Source licenses.
