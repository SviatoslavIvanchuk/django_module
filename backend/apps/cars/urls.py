from django.urls import path

from apps.cars.views import AddPhotoCarView, CarById, CarsList

urlpatterns = [
    path('', CarsList.as_view()),
    path('/<int:pk>', CarById.as_view()),
    path('/<int:pk>/photo', AddPhotoCarView.as_view())
]
