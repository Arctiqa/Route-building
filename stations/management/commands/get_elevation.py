from django.core.management import BaseCommand

from stations.models import GasStation
from stations.utils import get_open_elevation_elevation


class Command(BaseCommand):
    """Команда заполняет значения высоты над уровнем моря для заправочных станций"""

    def handle(self, *args, **options):
        stations = GasStation.objects.all()

        for station in stations:
            if station.elevation == ' ':
                try:
                    elevation = get_open_elevation_elevation(station.latitude, station.longitude)
                    station.elevation = elevation
                    station.save()
                except Exception as e:
                    print(station.latitude, station.longitude, e)
