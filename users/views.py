import json
import os.path
import uuid
from typing import TypedDict

from rest_framework.response import Response
from rest_framework.views import APIView

UserType = TypedDict('UserType', {'id': int, 'name': str, "email": str, "age": int, 'banned': bool})


class User(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__users: list[UserType] = []
        try:
            with open(os.path.dirname(__file__) + './../users.json') as file:
                self.__users: list[UserType] = json.load(file)
        except:
            pass

    def delete(self, *args, **kwargs):
        user_id = kwargs.get('id')
        file = open(os.path.dirname(__file__) + './../users.json', 'w')
        for user in self.__users:
            if user['id'] == user_id:
               self.__users.remove(user)
               json.dump(self.__users, file, indent=1)
               return Response(f'User with id: {user_id} Delete')
            else:
               json.dump(self.__users, file, indent=1)
               return Response(f'User with id: {user_id} not found')


    def get(self, *args, **kwargs):
        user_id = kwargs.get('id')
        for user in self.__users:
            if user['id'] == user_id:
                print(user)
                return Response(f'User with id: {user_id} -> {user}')
            else:
                return Response(f'User with id: {user_id} not found')

    def put(self, *args, **kwargs):
        update_user = self.request.data
        user_id = kwargs.get('id')
        file = open(os.path.dirname(__file__) + './../users.json', 'w')
        for user in self.__users:
            if user['id'] == user_id:
                user.update(update_user)
                json.dump(self.__users, file, indent=1)
                return Response(f'User with id: {user_id} Update -> {update_user}')
            else:
                return Response(f'User with id: {user_id} not found')


class UsersList(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__users: list[UserType] = []
        try:
            with open(os.path.dirname(__file__) + './../users.json') as file:
                self.__users: list[UserType] = json.load(file)
        except:
            pass

    def post(self, *args, **kwargs):
        create_user = self.request.data
        create_user['id'] = uuid.uuid4().time
        file = open(os.path.dirname(__file__) + './../users.json', 'w')
        self.__users.append(create_user)
        json.dump(self.__users, file, indent=1)
        return Response(create_user)

    def get(self, reques):
        return Response(self.__users)