from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ActivateUserView, RecoveryPasswordView, ChangePasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoveryPasswordView.as_view()),
    path('/recovery/<str:token>', ChangePasswordView.as_view())
]