from django.urls import path

from .views import ActivateUserView, AdminToUserView, DeActivateUserView, UserCreateView, UserToAdminView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/activate', ActivateUserView.as_view()),
    path('/<int:pk>/deactivate', DeActivateUserView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view())

]