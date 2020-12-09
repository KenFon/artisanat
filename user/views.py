from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from user.serializers import UserSerializer

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

