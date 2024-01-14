from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *
from .models import User

@api_view(['GET', 'POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':
        #queryset
        users = User.objects.all()
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        users_serializer = UserSerializer(data=request.data)
        #validation
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"message":"El usuario ha sido creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk=None):
    # queryset
    user = User.objects.filter(id=pk).first()

    #validation
    if user:

        #retrieve
        if request.method == 'GET':
            
            users_serializer = UserSerializer(user)
            return Response(users_serializer.data, status=status.HTTP_200_OK)
        
        #update
        elif request.method == 'PUT':
            user = User.objects.filter(id=pk).first()
            users_serializer = UserSerializer(user, data=request.data)
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data, status=status.HTTP_200_OK)
            return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({"message":"El usuario ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
        
    return Response({"message":"No se ha encontrado un usuario válido"}, status=status.HTTP_400_BAD_REQUEST)



# sistema de autenticación

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *arg, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data['access'],
                    'refresh-token': login_serializer.validated_data['refresh'],
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso'
                }, status=status.HTTP_200_OK)
        return Response({'message': 'Usuario y/o contraseña inválidos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user')).first()
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Logout exitoso'}, status=status.HTTP_200_OK)
        return Response({'message': 'No existe este usuario'}, status=status.HTTP_400_BAD_REQUEST)