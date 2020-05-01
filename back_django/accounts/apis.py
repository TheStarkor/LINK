from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import (
    UserListSerializer,
    LoginSerializer,
    SignupSerializer,
    FindAccountSerializer,
    PasswordResetSerializer,
)


# TODO : Token 처리


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class LoginAPI(CreateAPIView):
    serializer_class = LoginSerializer


class SignupAPI(CreateAPIView):
    serializer_class = SignupSerializer


class FindAccountAPI(CreateAPIView):
    serializer_class = FindAccountSerializer


class PasswordResetAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordResetSerializer
