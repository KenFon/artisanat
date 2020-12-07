from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Job, Profile
from .serializers import JobSerializer
from .forms import JobForm

# Create your views here.


@csrf_exempt
def jobs(request):
    """
    List all profiles, or create a new profile.
    """
    if request.method == 'GET':
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            serializer = JobSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def job(request, pk):
    """
    Retrieve, update or delete a job.
    """
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
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