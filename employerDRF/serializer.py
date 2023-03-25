from rest_framework import serializers
from .models import PostJobs,EmployerProfile


class EmployerProfileSerializer(serializers.Modelserializer):
    class meta:
        model = EmployerProfile
        fields = ["name","description","location","company","telephone","date_created","post_jobs"]


class PostJobSerializer(serializers.Modelserializer):
    class meta:
        model = PostJobs
        fields = ["description","job_location","experience_level","date_created","date_updated"]


