from datetime import datetime, timedelta

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import requests
from .models import WeatherData

from rest_framework import serializers, generics
from .models import WeatherData


API_KEY = "ade9f4cabec74e36b585f951ace85a05"
# API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

def send_data(request):

    return render(request, "index.html")


def get_weather_by_city(request, city=None):
    # Query the database for WeatherData objects with the given city_name



    if city:
        # Query the database for WeatherInfo objects with the given city name
        weather_info = WeatherData.objects.get(city=city)
        current_time = datetime.now(weather_info.updated_at.tzinfo)

        if current_time - weather_info.updated_at > timedelta(days=1):
            API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            try:
                response = requests.get(API_URL)
                if response.status_code == 200:
                    data = response.json()
                    updated_weather_data = {
                        "description": data['weather'][0]['description'],
                        "temperature": data['main']['temp'],
                        "pressure": data['main']['pressure'],
                        "icon": data['weather'][0]['icon']
                    }

                    weather_info = WeatherData.objects.create(
                        city=city,
                        description=updated_weather_data['description'],
                        temperature=updated_weather_data['temperature'],
                        pressure=updated_weather_data['pressure'],
                        icon=updated_weather_data['icon'],
                        updated_at=datetime.now()
                    )

                    weather_info = WeatherData.objects.get(city=city)
                    serialized_data = {
                        "city": weather_info.city,
                        "description": weather_info.description,
                        "temperature": weather_info.temperature,
                        "pressure": weather_info.pressure,
                        "icon": weather_info.icon,
                        "updated_at": weather_info.updated_at
                    }
                    # Return the serialized data as a JSON response
                    return JsonResponse(serialized_data)

            except Exception as e:
                print(f"Error fetching weather data: {e}")

        else:

            weather_info = WeatherData.objects.all().first()


            if weather_info:
                # Serialize the retrieved data
                serialized_data = {
                    "city": weather_info.city,
                    "description": weather_info.description,
                    "temperature": weather_info.temperature,
                    "pressure": weather_info.pressure,
                    "icon": weather_info.icon,
                    "updated_at": weather_info.updated_at
                }
                # Return the serialized data as a JSON response
                return JsonResponse(serialized_data)
            else:
                return JsonResponse({"error": "Weather information not found for the specified city"}, status=404)
