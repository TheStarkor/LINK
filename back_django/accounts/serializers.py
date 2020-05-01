from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "portal_id", "name", "dept_major", "username", "reputation")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("portal_id", "username", "email", "password")
        extra_kwards = {"password": {"write_only": True}}

    def creat_user(self, validated_data):
        if not validated_data["email"]:
            raise ValueError("User must have an email address")
        if not validated_data["username"]:
            raise ValueError("User must have an username")

        user = self.model.creat_user(
            validated_data["email"],
            validated_data["portal_id"],
            validated_data["name"],
            validated_data["dept_major"],
            validated_data["username"],
            validated_data["password"],
        )

        return user

    # def create_superuser(self, email, password, portal_id, name, dept_major, username):
    #     user = self.creat_user(
    #         email,
    #         password=password,
    #         portal_id = portal_id,
    #         name = name,
    #         dept_major = dept_major,
    #         username = username,
    #     )

    #     user.is_admin = True
    #     user.is_active = True
    #     user.is_email_verified = True

    #     user.save(using=self._db)
    #     return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()