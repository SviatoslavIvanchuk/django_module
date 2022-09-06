from django.db import models
from django.core import validators as v
from datetime import date
from apps.auto_parks.models import AutoParkModel


class CarsModel(models.Model):

    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField(validators=(v.MinValueValidator(1990), v.MaxValueValidator(date.today().year)), default=2000)
    price = models.IntegerField(validators=(v.MinValueValidator(0), v.MaxValueValidator(500000)), default=0)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)