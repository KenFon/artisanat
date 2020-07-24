from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from core.models import Job


class TestJobIndex(TestCase):

    def setUp(self):
        self.Job = Job.objects.create(profile=1, name="test Job", description="Test Job Index")

    def test_Job_index(self):
        """Tests that index path is showing Job data."""
        c = Client()
        response = c.get('/Job/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test Job')

class TestJobCreate(TestCase):

    def test_Job_create(self):
        """ Tests that the Job added has been created."""
        c = Client()
        data = {'profile': "4",'name':"test Job", 'description': "coucou"}
        response = c.post('/Jobs/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Job.objects.filter(name="test Job").exists())

class TestJobUpdate(TestCase):

    def setUp(self):
        Job.objects.create(profile=2, name="test Job", description="123")

    def test_Job_update(self):
        """Tests that the Job edited has been modified."""
        Job = Job.objects.last()
        c = Client()
        data = '{"name": "test Job update"}'
        response = c.put('/Jobs/'+str(Job.id)+'/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Job.objects.filter(name='test Job update').exists())

class TestJobDelete(TestCase):
    
    def setUp(self):
       Job.objects.create(profile= 3, name="test Job", description="delete")

    def test_Job_delete(self):
        """Tests that the Job deleted no longer exists."""
        Job = Job.objects.last()
        c = Client()
        response = c.delete('/Jobs/'+str(Job.id)+'/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Job.objects.filter(pk=Job.id).exists())