from django.urls import path

from .views import AutoParkAddCarView, AutoParkListCreate, AutoParkRetrieveDestroy

urlpatterns = [
    path('', AutoParkListCreate.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroy.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]