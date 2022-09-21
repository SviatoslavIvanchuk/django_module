from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from .models import CarsModel
from .serializers import AddPhotoToCarSerializer, CarSerializer
from core.pagination.page_paginator import PagePagination
from .filters import CarFilter


class CarsList(ListAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)
    pagination_class = PagePagination
    filterset_class = CarFilter

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
    permission_classes = (AllowAny,)

class AddPhotoCarView(UpdateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = AddPhotoToCarSerializer
    http_method_names = ('patch',)