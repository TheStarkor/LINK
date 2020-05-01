from rest_framework import status, serializers
from rest_framework.response import Response
from django.db.models import Q
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "portal_id",
            "name",
            "dept_major",
            "username",
            "reputation",
        )


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("portal_id", "username", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get("password"))
        user.save()

        return user


class PasswordResetSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(max_length=130, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "new_password")

    def update(self, instance, validated_data):
        username = validated_data["username"]
        old_password = validated_data["password"]
        new_password = validated_data["new_password"]

        if username == instance.username and instance.check_password(old_password):
            instance.set_password(new_password)
            instance.save()

            return instance

        else:
            # TODO: raise 400 error
            print("===========>400err")
            return instance


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(max_length=30)
    password = serializers.CharField(max_length=130, write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "id")

    def create(self, validated_data):
        user = User.objects.get(username=validated_data["username"])
        username = validated_data["username"]
        password = validated_data["password"]

        print(user, validated_data)

        if username == user.username and user.check_password(password):
            return user

        else:
            # TODO: raise 400 error
            print("===========>400err")
            return user


class FindSerializer(serializers.ModelSerializer):
    portal_id = serializers.CharField(max_length=10)
    portal_pw = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = User
        fields = ("portal_id", "portal_pw", "email")
        read_only_fields = ("email",)

    def create(self, validated_data):
        user = User.objects.get(portal_id=validated_data["portal_id"])

        if user:
            return user

        else:
            # TODO: none 처리 400 error
            return user
