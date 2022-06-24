from multiprocessing import managers
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
  path('', views.wetter, name="wetter"),
]