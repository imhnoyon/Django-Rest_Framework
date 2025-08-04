from django.shortcuts import render
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RegistrationViewsets(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegistrationSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):  
        request.user.auth_token.delete()
        return Response({'message': 'Token deleted successfully!'})
    