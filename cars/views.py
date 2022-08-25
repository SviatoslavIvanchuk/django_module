from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from .models import CarsModel
from .serializers import CarSerializer, CarSerializerForGetAll


class CarsList(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        qs = CarsModel.objects.all()
        serializer = CarSerializerForGetAll(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CarById(APIView):
    def get(self, *args, **kwargs):
        car_id = kwargs.get('id')
        car = get_object_or_404(CarsModel, pk=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        car_id = kwargs.get('id')
        car = get_object_or_404(CarsModel, pk=car_id)
        data = self.request.data
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        car_id = kwargs.get('id')
        car = get_object_or_404(CarsModel, pk=car_id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)