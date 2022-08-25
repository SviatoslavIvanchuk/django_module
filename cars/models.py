from django.db import models


class CarsModel(models.Model):

    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=25)
    engine = models.FloatField()