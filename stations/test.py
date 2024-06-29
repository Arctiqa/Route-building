import requests
from dotenv import load_dotenv
import os

load_dotenv()


def get_elevation_open_elevation(latitude, longitude):
    url = f'https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}'
    response = requests.get(url)
    data = response.json()
    elevation = data['results'][0]['elevation']
    return elevation


s = get_elevation_open_elevation(54.889460703205, 52.283269931245)

print(s)


def get_current_temperature(latitude, longitude):
    API_KEY = os.getenv('OPENWEATHERMAP_API')
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={latitude},{longitude}'
    response = requests.get(url)
    data = response.json()
    current_temperature = data['current']['temp_c']
    return current_temperature


w = get_current_temperature(54.889460703205, 52.283269931245)

print(w)
