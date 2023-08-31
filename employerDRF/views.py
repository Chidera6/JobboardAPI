from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from .serializer import *
from .models import Jobs,EmployerProfile
from rest_framework.permissions import IsAuthenticated



class EmployerProfileCreateView(generics.CreateAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer  
    permission_classes = [IsAuthenticated]
    
    def perform_create(self,serializer):
        user = self.request.user
        serializer.save(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class EmployerProfilesListView(generics.ListAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    ordering_fields = ['date_created']
    search_fields = ['company_name','industry']
    permission_classes = [IsAuthenticated]

    
class EmployerProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileDetailSerializer
    lookup_field = "user__username"

class JobCreateView(generics.CreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    
    def perform_create(self, serializer):
        employer = self.request.user
        serializer.save(employer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class JobListView(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    ordering_fields = ['date_created']
    search_fields = ['job_location']
    permission_classes = [IsAuthenticated]


class JobSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobDetailSerializer
    lookup_field = "user__username"

