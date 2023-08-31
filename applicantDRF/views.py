from django.shortcuts import render
from .models import ApplicantProfile,Application
from .serializer import ApplicantProfileSerializer,ApplicationSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class ApplicantProfileView(generics.ListCreateAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class ApplicantProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer

class ApplicantProfileListView(generics.ListCreateAPIView):
    queryset = ApplicantProfile.objects.all()
    serializer_class = ApplicantProfileSerializer
    ordering_fields = ['location','experience']
    search_fields = ['location','skills','years_of_experience']

class Applications(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

class ApplicationsListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


class ApplicationsSingleView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    