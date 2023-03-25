from rest_framework import serializers
from .models import PostJobs,EmployerProfile


class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = ["name","description","location","company","telephone","date_created"]


class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJobs
        fields = ["description","job_location","experience_level","date_created","date_updated",'employer_profile']


