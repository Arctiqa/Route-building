import os
import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

load_dotenv()


def get_open_elevation_elevation(latitude, longitude):
    """Получение данных о высоте над уровнем моря по координатам."""
    url = f'https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}'
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['results'][0]['elevation']


def get_weatherapi_temperature(latitude, longitude):
    """Получение данных о температуре по координатам."""
    API_KEY = os.getenv('WEATHERAPI_API')
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={latitude},{longitude}'
    response = requests.get(url, timeout=10)  # FIX: timeout
    response.raise_for_status()
    data = response.json()
    return data['current']['temp_c']


def get_tomtom_api_build_route(route):
    """Получение маршрута по координатам модели Route."""
    start_point = route.start_point.split()
    end_point = route.end_point.split()

    vehicle_type = 'car'

    if (
        (route.weight is not None and route.weight >= 36)
        or (route.height is not None and route.height >= 4)
        or (route.axel_load is not None and route.axel_load >= 9)
    ):
        vehicle_type = 'truck'

    url = (
        f'https://api.tomtom.com/routing/1/calculateRoute/'
        f'{start_point[0]},{start_point[1]}:{end_point[0]},{end_point[1]}/json'
    )
    params = {
        'key': os.getenv('TOMTOM_API'),
        'travelMode': vehicle_type,
    }

    try:
        response = requests.get(url, params=params, timeout=15)  # FIX: timeout
        response.raise_for_status()
        route_data = response.json()

        if 'routes' in route_data and route_data['routes']:
            points = route_data['routes'][0]['legs'][0]['points']
            summary = route_data['routes'][0]['summary']
            return [points, summary['lengthInMeters'], summary['travelTimeInSeconds']]
        return None

    except RequestException as e:
        print('Ошибка при запросе маршрута:', e)
        return None