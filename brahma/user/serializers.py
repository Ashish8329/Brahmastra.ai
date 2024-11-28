from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import CustomUser


class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "profile_picture",
        )

        read_only_fields = ("id",)

    def create(self, validated_data):
        """
        This will make the password as hassed
        """
        password = validated_data.pop("password")

        validated_data["password"] = make_password(password)
        return super().create(validated_data)
