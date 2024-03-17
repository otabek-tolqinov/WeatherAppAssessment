from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather_by_city, name="get_weather"),
    path('get-weather-by-city/<str:city>/', views.get_weather_by_city, name='get_weather_by_city'),
]
