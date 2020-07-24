from django.test import TestCase, Client
from core.models import Profile


class TestProfileIndex(TestCase):

    def setUp(self):
        self.profile = Profile.objects.create(type="A", name="test profile", description="123")

    def test_profile_index(self):
        """Tests that index path is showing profile data."""
        c = Client()
        response = c.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test profile')

class TestProfileCreate(TestCase):

    def test_profile_create(self):
        """ Tests that the profile added has been created."""
        c = Client()
        data = {'type': "A", 'name': "test profile", "description": "123"}
        response = c.post('/profiles/', data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Profile.objects.filter(name="test profile").exists())

class TestProfileUpdate(TestCase):

    def setUp(self):
        Profile.objects.create(type="A", name="test profile", description="123")

    def test_profile_update(self):
        """Tests that the profile edited has been modified."""
        profile = Profile.objects.last()
        c = Client()
        data = '{"name": "test profile update"}'
        response = c.put('/profiles/'+str(profile.id)+'/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Profile.objects.filter(name='test profile update').exists())

class TestProfileDelete(TestCase):
    
    def setUp(self):
       Profile.objects.create(type="A", name="test profile", description="delete")

    def test_profile_delete(self):
        """Tests that the profile deleted no longer exists."""
        profile = Profile.objects.last()
        c = Client()
        response = c.delete('/profiles/'+str(profile.id)+'/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Profile.objects.filter(pk=profile.id).exists())
