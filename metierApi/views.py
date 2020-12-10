from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Job, Profile
from jobs.serializers import JobSerializer
import json
import random
from django.core.exceptions import ObjectDoesNotExist
from collections import OrderedDict
# Create your views here.


@csrf_exempt
def result(request):
    """
    return top 3 jobs after game
    """
    # if !request.is_ajax():
    #     return JsonResponse(serializer.errors, status=404)

    # if request.method != 'POST':
    #     return JsonResponse('serializer.errors', status=404)

    data = json.loads(request.body)

    #récupère le profil 1 et tous les jobs en base de données avec le profil 1 sinon les met à none
    try:
        p1 = Profile.objects.get(type=data['profile_1'])
        jobs_p1 = Job.objects.filter(profile = p1.id) 
    except ObjectDoesNotExist:
        p1 = None
        jobs_p1 = None
    #récupère le profil 2 et tous les jobs avec le profil 2 sinon les met à none   
    try: 
        p2 = Profile.objects.get(type=data['profile_2'])
        jobs_p2 = Job.objects.filter(profile = p2.id)
    except ObjectDoesNotExist:
        p2 = None
        jobs_p2 = None
    #récupère le profil 3 et tous les jobs avec le profil 3 sinon les met à none
    try:
        p3 = Profile.objects.get(type=data['profile_3'])
        jobs_p3 = Job.objects.filter(profile = p3.id) 
    except ObjectDoesNotExist:
        p3 = None
        jobs_p3 = None

    #je crée une liste vide de jobs
    jobs = list()

    #jobs with all profile
    if p2 is not None and p3 is not None: 
        jobs_allr = jobs_p1.filter(
            profile = p2.id
        ).filter(
            profile = p3.id
        ).distinct()
        jobs = jobs + random.shuffle(list(jobs_allr))

    #jobs with profile 1 & 2
    if p2 is not None: 
        jobs_1_2 = jobs_p1.filter(
            profile = p2.id
        ).distinct()
        jobs = jobs + random.shuffle(list(jobs_1_2))

    #jobs with profile 1 & 3
    if p3 is not None:
        jobs_1_3 = jobs_p1.filter(
            profile = p3.id
        ).distinct()
        jobs = jobs + random.shuffle(list(jobs_1_3))

    #jobs with profile 2 & 3
    if p2 is not None and p3 is not None:
        jobs_2_3 = Job.objects.filter(
            profile = p1.id
        ).filter(
            profile = p3.id
        ).distinct()
        jobs = jobs + random.shuffle(list(jobs_2_3))

    #jobs with one of the 3 profile
    jobs_1r = jobs_p1
    if p2 is not None:
        jobs_1r = list(jobs_1r) + list(jobs_p2)
    if p3 is not None:
        jobs_1r = list(jobs_1r) + list(jobs_p3)
    OrderedDict.fromkeys(jobs_1r)
    jobs = jobs + random.shuffle(list(jobs_1r))

    jobs = OrderedDict.fromkeys(jobs)
    jobs = list(jobs)[:3]

    serializer = JobSerializer(jobs, many=True)
    return JsonResponse(serializer.data, safe=False)
