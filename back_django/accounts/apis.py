from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import User
from accounts.serializers import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer,
    PasswordResetSerializer,
    FindSerializer,
)


# TODO : Token 처리


class UserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginAPI(CreateAPIView):
    serializer_class = LoginSerializer


class SignupAPI(CreateAPIView):
    serializer_class = RegisterSerializer


class FindAccountAPI(CreateAPIView):
    serializer_class = FindSerializer


class PasswordResetAPI(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordResetSerializer
