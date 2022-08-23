from django.contrib import admin
from django.urls import path

from users.views import User, UsersList

urlpatterns = [
    path('users', UsersList.as_view()),
    path('users/<int:id>', User.as_view()),
]
