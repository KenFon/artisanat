from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework import generics
from core.models import Job, Profile
from job import serializers

# Create your views here.


class JobViewSet(viewsets.ModelViewSet):
    """Manage job in the database"""
    serializer_class = serializers.JobSerializer
    queryset = Job.objects.all()

    def get_queryset(self):
        return self.queryset

