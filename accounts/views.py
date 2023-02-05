from django.contrib.auth import logout
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts.serializers import RegisterSerializers, LoginSerializers, ProfileSerializers
from .models import Profile


class RegisterAPIView(APIView):
    def post(self, request):
        ser_data = RegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        ser_data = LoginSerializers(data=request.POST, context={'request': request})
        if ser_data.is_valid():
            user = ser_data.validated_data['user']
            update_last_login(None, user)
            token = Token.objects.get(user=user)
            return Response({"status": status.HTTP_200_OK, "Token": token.key})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ProfileShowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        ser_data = ProfileSerializers(instance=profile)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class ProfileUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        profile = Profile.objects.get(pk=pk)
        ser_data = ProfileSerializers(instance=profile, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

