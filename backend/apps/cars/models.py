from datetime import date

from django.core import validators as v
from django.db import models

from apps.auto_parks.models import AutoParkModel

from .managers import CarManager
from .services import upload_to


class CarsModel(models.Model):

    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=25)
    year = models.IntegerField(validators=(v.MinValueValidator(1990), v.MaxValueValidator(date.today().year)), default=2000)
    price = models.IntegerField(validators=(v.MinValueValidator(0), v.MaxValueValidator(500000)), default=0)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    photo = models.ImageField(upload_to=upload_to, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarManager()