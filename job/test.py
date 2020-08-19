# Create your tests here.
from django.urls import reverse
from rest_framework import status
from django.test import TestCase, Client
# import models
from core.models import Job, Profile
from job.serializers import JobSerializer
from profil.serializers import ProfileSerializer
from rest_framework.test import APIClient

JOB_URL = reverse
('job:job-list')

def sample_profile(**params):
    """create and return profile """
    datas={
             'type': "A",
             'name': "test le job",
             'description': "test small desc",
             } 
    datas.update(params)
    return Profile.objects.create(**datas)

def sample_job(**params):
    """create and return job """
    default={
            'name': "A",
            'bigDescription': "test le job",
            'smallDescription': "test small desc",
            'descFormation':"descformation",
            'video' : "lavideo"
            } 
    default.update(params)
    return Job.objects.create(**default)

class TestJobIndex(TestCase):

    def setUp(self):
       
        self.client = APIClient()

    def test_Job_index(self):

        """Tests that index path is showing Job data."""
        profile = sample_profile
        job = sample_job
        job.objects.add(profile)
        response = self.client.get(JOB_URL)
        jobs = job.objects.all()
        serializer = JobSerializer(jobs,many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
        self.assertContains(response, 'test Job')

class TestJobCreate(TestCase):

    def test_job_create(self):
        
        """ Tests that the job added has been created."""
        profile = sample_profile
        response = self.client.post(JOB_URL,profile)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Job.objects.filter(name="test le job").exists())
