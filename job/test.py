# Create your tests here.
from django.test import TestCase, Client
# import models
from core.models import Job, Profile




class TestJobIndex(TestCase):

    def setUp(self):

        self.Profile = Profile.objects.create(type="toto", name="test profil", description="Test profil")
        self.Job = Job.objects.create(name="test Job", bigDescription="Test Job Index")
        self.Job.profile.add(self.Profile)

    def test_Job_index(self):
        """Tests that index path is showing Job data."""
        c = Client()
        response = c.get('/jobs/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test Job')