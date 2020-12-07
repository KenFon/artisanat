# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
# import models
from core.models import Job, Profile


def detail_url(job_id):
    """Return job detail URL"""
    return reverse('jobs:jobs-detail', args=[job_id])

class TestJobIndex(TestCase):

    def setUp(self):

        self.Profile = Profile.objects.create(type="toto", name="test profil", description="Test profil")
        self.Job = Job.objects.create(name="test Job", bigDescription="Test Job Index")
        self.Job.profile.add(self.Profile)

    def test_job_index(self):
        """Tests that index path is showing Job data."""
        c = Client()
        response = c.get('/jobs/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test Job')

class TestJobCreate(TestCase):

    def test_job_create(self):
        """ Tests job added has been created."""
        c = Client()
        data = {'name': "test Job", 'bigDescription':"coucou", 'smallDescription':"petite"}
        response = c.post('/jobs/', data)
        self.assertEqual(response.status_code, 201 ,response.content)
        self.assertTrue(Job.objects.filter(smallDescription="petite").exists())

class TestJobUpdate(TestCase):

    def setUp(self):
        self.Profile = Profile.objects.create(type="toto", name="test profil", description="Test profil")
        self.Job = Job.objects.create(name="test Job", bigDescription="Test Job Index")
        self.Job.profile.add(self.Profile)

    def test_job_update(self): 
        """ Tests job added has been edited."""
        job = Job.objects.last()
        data = '{"name": "update job", "bigDescription": "Test Job Index"}'
        self.client.put("/jobs/"+str(job.id)+"/", data)
        job.refresh_from_db()
        self.assertEqual(job.name, "update job")

class TestJobDelete(TestCase):
    
    def setUp(self):
        self.Profile = Profile.objects.create(type="toto", name="test profil", description="Test profil")
        self.Job = Job.objects.create(name="test Job", bigDescription="Test Job Index")
        self.Job.profile.add(self.Profile)

    def test_job_delete(self):
        """Tests that the job deleted no longer exists."""
        job = Job.objects.last()
        self.client.delete('/jobs/'+str(job.id)+'/')
        self.assertFalse(Job.objects.filter(pk=job.id).exists())