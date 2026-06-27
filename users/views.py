from django.shortcuts import render
from users.serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,AllowAny


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def user_response_data(user):
    tokens = get_tokens_for_user(user)
    return {
        'id': user.id,
        'username': user.username,
        'refresh': tokens['refresh'],
        'access': tokens['access'],
    }



class UserRegisterView(APIView):
    permission_classes = [AllowAny]  
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({**user_response_data(user), **get_tokens_for_user(user)},status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        user=serializer.validate_data['user']

        return Response(
            {**user_response_data(user), **get_tokens_for_user(user)},
            status=status.HTTP_200_OK,
        )

           
    

class UserLogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)