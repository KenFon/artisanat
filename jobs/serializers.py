from rest_framework import serializers
from core.models import Job



class JobSerializer(serializers.Serializer):

    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    bigDescription = serializers.CharField(required=False, allow_blank=True, max_length=100)
    smallDescription = serializers.CharField(required=False, allow_blank=True, max_length=100)
    descFormation = serializers.CharField(required=False, allow_blank=True, max_length=100)
    video = serializers.CharField(required=False, allow_blank=True, max_length=100)
    #SimilarJob = serializers(read_only=True, many=True)
    profile = serializers.PrimaryKeyRelatedField(read_only=True, many=True)


    def create(self, validated_data):
        """Create and return a new profile instance given the validated data"""
        return Job.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing Job instance, given the validated data."""
        instance.name = validated_data.get('name', instance.name)
        instance.bigDescription = validated_data.get('bigDescription', instance.bigDescription)
        instance.smallDescription = validated_data.get('smallDescription', instance.smallDescription)
        instance.descFormation = validated_data.get('descFormation', instance.descFormation)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        return instance