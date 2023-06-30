import requests
import json

API_KEY = "your_api_key" # replace with your API key
CITY = "Moscow"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
URL = BASE_URL + "?q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
     data = response.json()
     main = data['main']
     temperature = main['temp']
     humidity = main['humidity']
     weather_report = data['weather']
     print(f"Temperature: {temperature 273.15}")
     print(f"Humidity: {humidity}")
     print(f"Weather: {weather_report[0]['description']}")
else:
     print("Error in API")
