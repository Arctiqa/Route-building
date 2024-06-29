from django.utils import timezone

from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=150, verbose_name='маршрут')
    start_point = models.CharField(max_length=100, verbose_name='начальный пункт')
    end_point = models.CharField(max_length=100, verbose_name='конечный пункт')
    length = models.IntegerField(verbose_name='длина маршрута')
    description = models.TextField(verbose_name='описание')
    date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    class Meta:
        verbose_name = 'маршрут'
        verbose_name_plural = 'маршруты'


class GasStation(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название АЗС')
    coordinates = models.CharField(max_length=50, verbose_name='Координаты')
    address = models.TextField(verbose_name='Адрес')
    diesel_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена дизельного топлива')
    elevation = models.IntegerField(verbose_name='Высота над уровнем моря')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'


class Refueling(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='Маршрут')
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE, verbose_name='АЗС')
    fuel_volume = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Объем топлива')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    refuel_date = models.DateTimeField(verbose_name='Дата и время заправки')

    class Meta:
        verbose_name = 'Заправка на маршруте'
        verbose_name_plural = 'Заправки на маршрутах'
