from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_data, name='send_data'),
    path('get-weather-by-city/<str:city>/', views.get_weather_by_city, name='get_weather_by_city'),
]
