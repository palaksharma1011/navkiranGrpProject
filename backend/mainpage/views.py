from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from .models import user
# Create your views here.

class UserList(ListAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer