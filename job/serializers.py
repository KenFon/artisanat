from rest_framework import serializers
from core.models import Job


class JobSerializer(serializers.Serializer):

    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=255)
    profile = serializers.IntegerField(required=False, allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """Create and return a new profile instance given the validated data"""
        return  Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `Profile` instance, given the validated data."""
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.save()
        return instance