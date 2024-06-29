import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда загружает таблицу с заправочными станциями с сайта rss.tatneft.ru"""
    def handle(self, *args, **options):

        url = 'https://rss.tatneft.ru/outer/azs/get_xml_list?region_id=0&fuel_type_id=0'
        file_path = 'gas_stations.xls'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при выполнении запроса: {e}')
        except IOError as e:
            print(f'Ошибка при сохранении файла: {e}')
