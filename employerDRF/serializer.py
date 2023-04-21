from rest_framework import serializers
from .models import PostJobs,EmployerProfile,CustomUser
from djoser.serializers import UserCreateSerializer

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',"username", 'first_name','last_name', 'email', 'user_type',"password",]

class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer(many=True,read_only=True)
    class Meta:
        model = EmployerProfile
        fields = ["id","description","location","company","telephone","date_created","user"]

class PostJobSerializer(serializers.ModelSerializer):
    employer_profile = EmployerProfileSerializer(many=True,read_only=True)
    class Meta:
        model = PostJobs
        fields = ["id","description","job_location","experience_level","date_created","date_updated",'employer_profile']

