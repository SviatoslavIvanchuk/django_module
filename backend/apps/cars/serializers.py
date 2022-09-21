from rest_framework.serializers import ModelSerializer

from .models import CarsModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'year', 'price')


class CarSerializerForGetAll(ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('id', 'brand', 'year')


class AddPhotoToCarSerializer(ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ('photo',)