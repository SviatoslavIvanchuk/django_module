from django.urls import path

from apps.cars.views import CarsList, CarById

urlpatterns = [
    path('', CarsList.as_view()),
    path('/<int:id>', CarById.as_view())
]