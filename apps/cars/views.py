from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import params_filter
from .models import CarsModel
from .serializers import CarSerializer


class CarsList(ListCreateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'GET':
            return CarSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return params_filter(queryset, self.request)


class CarById(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer