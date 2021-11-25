from pathlib import Path

from django.db import models


def get_upload_path(instance, filename):
    return Path(instance.name) / filename


class Spaceship(models.Model):
    owner = models.CharField(max_length=20, verbose_name='компания-владелец')
    name = models.CharField(max_length=20,
                            verbose_name='название корабля')
    flight_price = models.PositiveIntegerField(verbose_name='цена полета')
    capacity = models.PositiveSmallIntegerField(verbose_name='вместимость')
    image = models.ImageField(upload_to=get_upload_path,
                              verbose_name='изображение')

    class Meta:
        verbose_name = 'корабль'
        verbose_name_plural = 'корабли'

    def __str__(self):
        return self.name


class Order(models.Model):
    ship = models.ForeignKey(to=Spaceship, on_delete=models.CASCADE,
                             verbose_name='корабль')
    passenger = models.CharField(
        max_length=10, verbose_name='пассажир', blank=True
    )
    flight_date = models.DateField(verbose_name='дата полета')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
