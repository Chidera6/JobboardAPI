from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from serializer import PostJobSerializer,EmployerProfileSerializer
from .models import PostJobs,EmployerProfile

class EmployerProfileView(generics.ListCreateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer


class EmployerProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer

class PostJobView(generics.ListCreateAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobSerializer


class PostJobView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobSerializer