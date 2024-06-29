from django.utils import timezone

from django.db import models

from config import settings


class Route(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    start_point = models.CharField(max_length=255, verbose_name='координаты отправки')
    end_point = models.CharField(max_length=255, verbose_name='координаты прибытия')
    length = models.IntegerField(verbose_name='длина авто(метры)')
    height = models.FloatField(verbose_name='высота от земли(метры)')
    weight = models.FloatField(verbose_name='вес авто(тонны)')
    axle_load = models.FloatField(verbose_name='нагрузка на ось(тонны)')
    date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    class Meta:
        verbose_name = 'маршрут'
        verbose_name_plural = 'маршруты'


class GasStation(models.Model):
    region = models.CharField(max_length=200, verbose_name='Регион', null=True, blank=True)
    number = models.CharField(max_length=150, verbose_name='Номер АЗС', null=True, blank=True)
    latitude = models.CharField(max_length=50, verbose_name='Широта', null=True, blank=True)
    longitude = models.CharField(max_length=50, verbose_name='Долгота', null=True, blank=True)
    related_service = models.TextField(verbose_name='Сопутствующий сервис', null=True, blank=True)
    additional_service = models.TextField(verbose_name='Дополнительные услуги', null=True, blank=True)
    diesel_price = models.CharField(max_length=50, verbose_name='Цена ДТ', null=True, blank=True)
    taneko_diesel_price = models.CharField(max_length=50, verbose_name='Цена ДТ ТАНЕКО', null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'


class Refueling(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE, verbose_name='АЗС')

    class Meta:
        verbose_name = 'Заправка на маршруте'
        verbose_name_plural = 'Заправки на маршрутах'
