from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from firebase_auth.authentication import FirebaseAuthentication

class UserSerializer(serializers.ModelSerializer):
    """Serialiser for the users object"""

    class Meta:
        model = get_user_model()
        
        def create(self, request):
            data = request.data
            return FirebaseAuthentication.authenticate(data.uid)