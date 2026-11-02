from django.utils import timezone
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Route(models.Model):
    name = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Имя маршрута'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь'
    )
    start_point = models.CharField(max_length=255, verbose_name='Координаты отправки')
    end_point = models.CharField(max_length=255, verbose_name='Координаты прибытия')
    height = models.FloatField(
        verbose_name='Высота от земли (метры)',
        null=True, blank=True,
        validators=[MinValueValidator(0)],
    )
    weight = models.FloatField(
        verbose_name='Вес авто (тонны)',
        null=True, blank=True,
        validators=[MinValueValidator(0)],
    )
    axel_load = models.FloatField(
        verbose_name='Нагрузка на ось (тонны)',
        null=True, blank=True,
        validators=[MinValueValidator(0)],
    )
    date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')

    class Meta:
        verbose_name = 'маршрут'
        verbose_name_plural = 'маршруты'
        ordering = ['-date']


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
    elevation = models.CharField(
        max_length=10, null=True, blank=True, verbose_name='высота над уровнем моря'
    )

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'
        constraints = [
            models.UniqueConstraint(
                fields=['latitude', 'longitude'], name='unique_station_coords'
            )
        ]