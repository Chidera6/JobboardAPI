from rest_framework import serializers
from .models import Jobs,EmployerProfile,CustomUser
from djoser.serializers import UserCreateSerializer,UserSerializer

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ['id',"username", 'first_name','last_name', 'email', 'user_type',"password"]
        
class UserDetailSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ['id',"username", 'first_name','last_name', 'email', 'user_type',"password",]

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class EmployerProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobDetailSerializer(serializers.ModelSerializer):
    employer_profile = EmployerProfileDetailSerializer(read_only=True)
    class Meta:
        model = Jobs
        fields = '__all__'



