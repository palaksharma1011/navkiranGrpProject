from rest_framework import serializers
from .models import newuser

class newUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = newuser
        fields = ['firstname', 'lastname', 'email', 'password', 'mobilenum']