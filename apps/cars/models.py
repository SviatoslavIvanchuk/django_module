from django.db import models


class CarsModel(models.Model):

    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=25)
    year = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)