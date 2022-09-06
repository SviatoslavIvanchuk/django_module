from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .filters import params_filter
from .models import CarsModel
from .serializers import CarSerializer


class CarsList(ListAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('id')
        return queryset


class CarById(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer