from rest_framework_simplejwt.tokens import Token, BlacklistMixin
from core.enums.action_enum import ActionEnum
from core.exceptions.jwt_exception import JwtException
from rest_framework.generics import get_object_or_404

from typing import Type
from django.contrib.auth import get_user_model
from apps.users.models import UserModel as User

UserModel: Type[User] = get_user_model()


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.exp_time
    token_type = ActionEnum.ACTIVATE.token_type


class RecoveryToken(BlacklistMixin, Token):
    lifetime = ActionEnum.RECOVERY.exp_time
    token_type = ActionEnum.RECOVERY.token_type


class JwtService:
    @staticmethod
    def create_token(user, token_class: Type[BlacklistMixin | Token]):
        return token_class.for_user(user)

    @staticmethod
    def valid_token(token, token_class: Type[BlacklistMixin | Token]):
        try:
            activate_token = token_class(token)
            activate_token.check_blacklist()
        except (Exception, ):
            raise JwtException

        activate_token.blacklist()
        user_id = activate_token.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)