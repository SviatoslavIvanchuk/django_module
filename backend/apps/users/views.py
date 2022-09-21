from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.users.models import UserModel as User

from .permissins import IsSuperUser
from .serializers import AddAvatarSerializer, UserSerializer

UserModel: Type[User] = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return IsSuperUser(),
        return super().get_permissions()


class __AdminPermissionView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class ActivateUserView(__AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            user.is_active = True
            user.save()
        return Response(self.get_serializer(user).data, status.HTTP_200_OK)


class DeActivateUserView(__AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_active:
            user.is_active = False
            user.save()
        return Response(self.get_serializer(user).data, status.HTTP_200_OK)


class UserToAdminView(__AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if not user.is_staff:
            user.is_staff = True
            user.save()
        return Response(self.get_serializer(user).data, status.HTTP_200_OK)


class AdminToUserView(__AdminPermissionView):
    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.is_staff:
            user.is_staff = False
            user.save()
        return Response(self.get_serializer(user).data, status.HTTP_200_OK)
    
    
class AddAvatarView(UpdateAPIView):
    serializer_class = AddAvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile