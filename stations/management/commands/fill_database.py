from django.core.management import BaseCommand

import pandas as pd
from stations.models import GasStation
import xlrd


class Command(BaseCommand):
    """Команда заполняет таблицу stations_gasstation в БД информацией заправочных станций
    из файла """

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
                    pd.isnull(row['Объекты сопутствующего сервиса']) else None,
                    additional_service=row['Дополнительные услуги'],
                    diesel_price=(row['ДТ']) if not pd.isnull(row['ДТ']) else None,
                    taneko_diesel_price=(row['ДТ ТАНЕКО']) if not pd.isnull(row['ДТ ТАНЕКО']) else None,
                )
                gas_station.save()

            else:

                gas_station = GasStation.objects.get(latitude=str(row['Координаты GPS (широта)']),
                                                     longitude=str(row['Координаты GPS (долгота)']))
                gas_station.region = row['Регион'],
                gas_station.number = row['Номер АЗС'],
                gas_station.related_service = ((row['Объекты сопутствующего сервиса'])
                                               if not pd.isnull(row['Объекты сопутствующего сервиса']) else None,)
                gas_station.additional_service = row['Дополнительные услуги'],
                gas_station.diesel_price = (row['ДТ']) if not pd.isnull(row['ДТ']) else None,
                gas_station.taneko_diesel_price = (row['ДТ ТАНЕКО']) if not pd.isnull(row['ДТ ТАНЕКО']) else None,

                gas_station.save()
