from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Job, Profile
from .serializers import JobSerializer
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.



@csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def jobs(request):
    """
    List all profiles, or create a new profile.
    """
    if request.method == 'GET':
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return JsonResponse(serializer.data, safe=False)



@csrf_exempt
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def job(request, pk):
    """
    Retrieve, update or delete a job.
    """
    try:
        job = job.objects.get(pk=pk)
    except job.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = JobSerializer(job, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        job.delete()
        return HttpResponse(status=204)

