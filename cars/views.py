from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import CarsModel


class CarsList(APIView):

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarsModel(**data)
        car.save()
        return Response('Car created')

    def get(self, *args, **kwargs):
        qs = CarsModel.objects.all()
        res = [model_to_dict(car) for car in qs]
        return Response(res)


class CarbyId(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
