from django.core.management import BaseCommand

import pandas as pd
from stations.models import GasStation
import xlrd
from django.utils import timezone


class Command(BaseCommand):
    """Команда заполняет таблицу stations_gasstation в БД информацией заправочных станций из файла """

    def handle(self, *args, **options):
        workbook = xlrd.open_workbook('gas_stations.xls', ignore_workbook_corruption=True)
        df = pd.read_excel(workbook)

        for index, row in df.iterrows():
            check_gas_station = GasStation.objects.filter(latitude=str(row['Координаты GPS (широта)']),
                                                          longitude=str(row['Координаты GPS (долгота)']))
            if not check_gas_station:
                gas_station = GasStation(
                    region=row['Регион'],
                    number=row['Номер АЗС'],
                    latitude=str(row['Координаты GPS (широта)']),
                    longitude=str(row['Координаты GPS (долгота)']),
                    related_service=(row['Объекты сопутствующего сервиса']) if not
                    pd.isnull(row['Объекты сопутствующего сервиса']) else ' ',
                    additional_service=(row['Дополнительные услуги']) if not
                    pd.isnull(row['Дополнительные услуги']) else ' ',
                    diesel_price=(row['ДТ']) if not pd.isnull(row['ДТ']) else ' ',
                    taneko_diesel_price=(row['ДТ ТАНЕКО']) if not pd.isnull(row['ДТ ТАНЕКО']) else ' ',
                )
                gas_station.save()

            else:

                gas_station = GasStation.objects.get(latitude=str(row['Координаты GPS (широта)']),
                                                     longitude=str(row['Координаты GPS (долгота)']))
                gas_station.region = row['Регион'],
                gas_station.number = row['Номер АЗС'],
                gas_station.related_service = ((row['Объекты сопутствующего сервиса'])
                                               if not pd.isnull(row['Объекты сопутствующего сервиса']) else ' ',)
                gas_station.additional_service = ((row['Дополнительные услуги'])
                                                  if not pd.isnull(row['Дополнительные услуги']) else ' ',)
                gas_station.diesel_price = (row['ДТ']) if not pd.isnull(row['ДТ']) else ' ',
                gas_station.taneko_diesel_price = (row['ДТ ТАНЕКО']) if not pd.isnull(row['ДТ ТАНЕКО']) else ' ',
                gas_station.last_updated = timezone.now
                gas_station.save()
