from django.urls import path

from .views import AutoParkListCreate, AutoParkAddCarView

urlpatterns = [
    path('', AutoParkListCreate.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]