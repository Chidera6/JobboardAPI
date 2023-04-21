from django.shortcuts import render
from .models import ApplicantProfile
from .serializer import ApplicantProfileSerializer
from rest_framework import generics,status
from rest_framework.response import Response


class ApplicantProfileView(generics.ListCreateAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    ordering_fields = ['location','skills']

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class ApplicantProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer

#search candidates based on location,based on skills,based on experience level