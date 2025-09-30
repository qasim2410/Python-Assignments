import requests

from pprint import pprint

API_Key = 'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}'

city = input("Enter the city name: ")


base_url="https://openweathermap.org/api"+API_Key+"&q="+city


weather_data = requests.get(base_url).json()

pprint(weather_data)



