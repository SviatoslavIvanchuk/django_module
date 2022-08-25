from rest_framework.serializers import ModelSerializer

from .models import CarsModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'year', 'seats', 'body_type', 'engine')


class CarSerializerForGetAll(ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'year')