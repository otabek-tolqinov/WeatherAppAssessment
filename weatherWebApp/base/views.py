from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import requests
from .models import WeatherData

from rest_framework import serializers, generics
from .models import WeatherData


API_KEY = "ade9f4cabec74e36b585f951ace85a05"


def send_data(request):
    if request.method == "GET":
        city = "Birmingham"

        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(api_url)

        if response.status_code == 200:
            weather_data = response.json()
            description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            pressure = weather_data['main']['pressure']
            icon = weather_data['weather'][0]['icon']

            WeatherData.objects.create(
                description=description,
                temperature=temperature,
                pressure=pressure,
                icon=icon,
                city=city
            )

    return render(request,"index.html")


def get_weather_by_city(request, city):
    # Query the database for WeatherData objects with the given city_name

    city_name = city

    if city_name:
        # Query the database for WeatherInfo objects with the given city name
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
    else:
        return JsonResponse({"error": "No city name provided"}, status=400)




