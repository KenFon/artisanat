from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from user.serializers import UserSerializer

# Create your views here.
class CreateUserView(viewsets.ModelViewSet):
    """Create a new user in the system"""
    serializer_class = UserSerializer.create
