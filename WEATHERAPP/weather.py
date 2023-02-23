import datetime as dt
import requests

#weather website url
BASE_URL= "https://api.openweathermap.org/data/2.5/weather?"

#Api key to retrive information of weather
API_KEY= "63d6e858c8695891f38c170db1ae8bb5" 

#search city
print("Search City: ")
CITY= input()
print("CITY: " + CITY )

#function to convert °K(kelvin) to °C(celsius) and °F(Fahrenheit)
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

#final URL
url= BASE_URL + "appid=" + API_KEY + "&q=" + CITY

#sending request
response = requests.get(url).json()

#prints infromation
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

#Printing out Temperature, feels like, humidity, wind speed, description, sunrise, sunset
print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit: .2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}mph")
print(f"General weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")