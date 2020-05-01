from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bcrypt import hashpw, gensalt

from accounts.models import User
from accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer


# TODO : Token 처리
# signup -> SignupAPI
# landing -> LoginAPI
# find_account -> FindAccountAPI
# pw_reset -> PasswordResetAPI


class SignupAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        request.data["password"] = encrypt(request.data["password"])
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({"user": {"email": user.email, "username": user.name,}})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        request.data["password"] = encrypt(request.data["password"])
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            return Response({"username": user["username"],})

        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTETN)


# class FindAccountAPI(generics.GenericAPIView):
# class PasswordResetAPI(generic.GenericAPIView):


def encrypt(password):
    return hashpw(password.encode("utf-8"), gensalt()).hex()
