from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from user.models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "password",
            "role"
        )

        read_only_fields = ("id",)
    
    def create(self, validated_data):
        """
        Override the create method to hash the user's password.
        """
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)

        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "profile_picture",
            "role",
        )

        read_only_fields = ("id",)
    
    def to_representation(self, instance):
        """
        Remove the password field from response.
        """
        data = super().to_representation(instance)
        data.pop("password")
        return data
    

    def create(self, validated_data):
        """
        Override the create method to hash the user's password.
        """
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)

        return super().create(validated_data)
