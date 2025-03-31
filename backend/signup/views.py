
from .serializers import newUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
def register_user(request):
    data = request.data
    if User.objects.filter(email=data['email']).exists():
        return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        password=make_password(data['password']),  # Hash the password!
        mobilenum=data['mobilenum']
    )
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

