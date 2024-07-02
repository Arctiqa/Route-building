import math
import os

import requests
from dotenv import load_dotenv
from requests.exceptions import RequestException

load_dotenv()


def get_open_elevation_elevation(latitude, longitude):
    """Получение данных о расстоянии над уровнем моря по координатам"""
    url = f'https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}'
    response = requests.get(url)
    data = response.json()
    elevation = data['results'][0]['elevation']
    return elevation


def get_weatherapi_temperature(latitude, longitude):
    """Получение данных о температуре по координатам"""
    API_KEY = os.getenv('WEATHERAPI_API')
    url = f'https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={latitude},{longitude}'
    response = requests.get(url)
    data = response.json()
    current_temperature = data['current']['temp_c']
    return current_temperature


def get_tomtom_api_build_route(route):
    """Получения маршрута по координатам модели Route"""
    start_point = route.start_point.split()
    end_point = route.end_point.split()

    vehicle_type = 'car'

    if (route.weight is None or route.weight >= 36 and route.height is None or
            route.height >= 4 and route.axel_load is None or route.axel_load >= 9):
        vehicle_type = 'truck'

    url = (f'https://api.tomtom.com/routing/1/calculateRoute/{start_point[0]},{start_point[1]}:'
           f'{end_point[0]},{end_point[1]}/json')

    params = {
        'key': os.getenv('TOMTOM_API'),
        'travelMode': vehicle_type,
        # 'routeType': 'fastest'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        route_data = response.json()
        points = route_data['routes'][0]['legs'][0]['points']

        lengthInMeters = route_data['routes'][0]['summary']['lengthInMeters']
        travelTimeInSeconds = route_data['routes'][0]['summary']['travelTimeInSeconds']

        if 'routes' in route_data and len(route_data['routes']) > 0:
            return [points, lengthInMeters, travelTimeInSeconds]
        else:
            return None

    except RequestException as e:
        print('Ошибка при запросе маршрута:', e)
        return None


# def get_nearest_stations(route_points, stations):
#     R = 6371.0
#
#     stations = stations.objects.all().value('latitude', 'longitude')
#
#     # Преобразование градусов в радианы
#     lat1 = math.radians(lat1)
#     lon1 = math.radians(lon1)
#     lat2 = math.radians(lat2)
#     lon2 = math.radians(lon2)
#
#     # Разницы широты и долготы
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#
#     a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#
#     distance = R * c
#
#     return distance

# def gas_stations_on_route(requests, pk):
#     points = get_tomtom_api_build_route(requests, pk)
#
#     if points:
#         stations = GasStation.objects.all().values('latitude', 'longitude')
#         stations_list = list(stations)
#         stations_near_route = []
#
#         for station in stations_list:
#             # Проверяем, находится ли автозаправка рядом с какой-либо из точек маршрута
#             for point in points:
#                 distance = calculate_distance(station.latitude, station.longitude, point['latitude'],
#                                               point['longitude'])
#                 if distance < 1000:
#                     stations_near_route.append({
#                         'latitude': station.latitude,
#                         'longitude': station.longitude,
#                         'number': station.number
#                     })
#                     break
#
#         return JsonResponse(stations_near_route, safe=False)
#     else:
#         return JsonResponse({'error': 'Маршрут не найден или не удалось построить маршрут.'}, status=404)
