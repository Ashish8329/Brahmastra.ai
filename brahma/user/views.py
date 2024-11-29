from base.utils import error_response, success_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.shortcuts import redirect, render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from user.models import CustomUser
from user.serializers import UserSerializer, RegistrationSerializer
from user.utils import get_tokens_for_user
from strings import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone



class RegistrationAPI(viewsets.ModelViewSet):
    """
    API View for user registration in the system.
    """
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description="This API registers a user in the system.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.FORMAT_EMAIL, description="User Email"
                ),
                "password": openapi.Schema(
                    type=openapi.FORMAT_PASSWORD, description="User Password"
                ),
            },
        ),
        responses={201: openapi.Response(REGISTRATION_SUCCESS)},
    )
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        Handle user registration.

        Validates the request data, saves the user instance, and returns the
        user details along with authentication tokens.

        Returns:
            Response: A success response containing the user data and tokens.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.save()

        return success_response(
            data=serializer.data,
            message=REGISTRATION_SUCCESS,
            extra_data={
                "token": get_tokens_for_user(user_instance)  # handle jwt token
            },
        )


class LoginAPIView(viewsets.ModelViewSet):
    """
    API View for user authentication and login.

    Authenticates a user using email and password and logs them into the system.
    """
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_description="This API authenticates and logs in a user.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(
                    type=openapi.FORMAT_EMAIL, description="User Email"
                ),
                "password": openapi.Schema(
                    type=openapi.FORMAT_PASSWORD, description="User Password"
                ),
            },
        ),
        responses={201: openapi.Response(LOGIN_SUCCESS)},
    )
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        Handle user login.

        Validates user credentials and logs them into the system.

        Args:
            request: The HTTP request containing login credentials.

        Returns:
            Response: A success response if authentication is successful,
            otherwise an error response.
        """
        email = request.POST.get("email")
        password = request.POST.get("password")
        authenticated_user = authenticate(request, email=email, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)

            # Serialize user data
            user_data = UserSerializer(authenticated_user).data

            return success_response(
                message=LOGIN_SUCCESS,
                data=user_data,
                extra_data={
                    "token":  get_tokens_for_user(authenticated_user)  # handle jwt token
                },
            )
        else:
            return error_response(
                message=AUTHENTICATION_FAILED
            )


class LogoutAPIView(APIView):
    """
    API View for user logout.

    Logs out a user from the system and invalidates their session.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="This API logs out a user from the system.",
        responses={201: LOGOUT_SUCCESS},
    )
    @transaction.atomic
    def post(self, request):
        logout(request)
        return success_response(message=LOGOUT_SUCCESS)