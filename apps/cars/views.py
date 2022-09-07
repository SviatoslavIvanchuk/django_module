from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .models import CarsModel
from .serializers import AddPhotoToCarSerializer, CarSerializer


class CarsList(ListAPIView):
    queryset = CarsModel.objects.get_by_price_gt(5000)
    serializer_class = CarSerializer
    permission_classes = (IsAdminUser,)

    # def get_queryset(self):
    #     auto_park_id = self.request.query_params.get('autoParkId')
    #     if auto_park_id:
    #         return self.queryset.filter(auto_park_id=auto_park_id)
    #     queryset = super().get_queryset()
    #     queryset = queryset.order_by('id')
    #     return queryset


class CarById(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer


class AddPhotoCarView(UpdateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = AddPhotoToCarSerializer
    http_method_names = ('patch',)