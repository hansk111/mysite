from django.shortcuts import render
import requests
from .models import City
# Create your views here.

def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=54005e91865c1dd6651460dd3bfb88e7'
    
    cities = City.objects.all() #return all the cities in the database
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city.name)).json() #request the API data and convert the JSON to Python data types
        print(city_weather)
        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data}
    return render(request, 'weather/weather.html', context )

    # url = 'http://apis.data.go.kr/1360000/VilageFcstInfoServiceget/VilageFcst?serviceKey=TYrk4SWa%2F59LmQoSi2jZnJvw2zu%2FFDBbN4aDLVVWOxc9HUB6heFw%2FKPOCoxRJfaQKuPDAdTdwZd1LQvBXzGxDw%3D%3D&numOfRows=10&pageNo=1&dataType=JSON&base_date=20210824&base_time=1200&nx=635&ny=123'

    # weather_test = requests.get(url).json()
    # logger.info(type(response))
    # # print(weather_test)
    # weather = {
    #     'city' : 'city',
    #     'temperature' : weather_test['response']['body']['dataType'],
    # #     'description' : weather_test['response']['body']['dataType'],
    # #     'icon' : weather_test['response']['body']['dataType']
    # }
    # context = {'weather' : weather}
    # return render(request, 'weather/weather.html', context )