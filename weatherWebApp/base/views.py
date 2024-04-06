from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import requests
from .models import WeatherData

from rest_framework import serializers, generics
from .models import WeatherData


API_KEY = "ade9f4cabec74e36b585f951ace85a05"


def send_data(request):

    return render(request, "index.html")


# def get_weather_by_city(request, city=None):
#     # Query the database for WeatherData objects with the given city_name
#
#     city_name = "Birmingham"
#
#     if city_name:
#         # Query the database for WeatherInfo objects with the given city name
#         weather_info = WeatherData.objects.all().first()
#
#         if weather_info:
#             # Serialize the retrieved data
#             serialized_data = {
#                 "city": weather_info.city,
#                 "description": weather_info.description,
#                 "temperature": weather_info.temperature,
#                 "pressure": weather_info.pressure,
#                 "icon": weather_info.icon,
#                 "updated_at": weather_info.updated_at
#             }
#             # Return the serialized data as a JSON response
#             return JsonResponse(serialized_data)
#         else:
#             return JsonResponse({"error": "Weather information not found for the specified city"}, status=404)
#     else:
#         return JsonResponse({"error": "No city name provided"}, status=400)
#
#
#





