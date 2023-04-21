from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from .serializer import PostJobSerializer,EmployerProfileSerializer
from .models import PostJobs,EmployerProfile

class EmployerProfileView(generics.ListCreateAPIView):
    queryset = EmployerProfile.objects.all().select_related('user')
    serializer_class = EmployerProfileSerializer  
    search_fields = ['location']

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class EmployerProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerProfile.objects.all().select_related('user')
    serializer_class = EmployerProfileSerializer

class PostJobView(generics.ListCreateAPIView):
    queryset = PostJobs.objects.all()
    serializer_class = PostJobSerializer
    ordering_fields = ['date_created']
    search_fields = ['experience_level','job_location','date_created']

    def perform_create(self, serializer):
        employer = self.request.user
        serializer.save(employer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class PostJobSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJobs.objects.all().select_related('employer_profile')
    serializer_class = PostJobSerializer