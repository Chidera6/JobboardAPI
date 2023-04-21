from django.db import models
from django.contrib.auth.models import AbstractUser,User

class CustomUser(AbstractUser):
    "A custom user models for all the users"
    USER_TYPE_CHOICES = ("1","Admin"),("2","Employer"),("3","Applicant")
    user_type = models.PositiveIntegerField(default="3",null=True,choices=USER_TYPE_CHOICES)
    def __str__(self):
        return self.username
  
   
class EmployerProfile(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    telephone = models.PositiveIntegerField(null=True)
    avatar = models.ImageField(null=True,upload_to='images/users',blank=True) 
    company = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    
    def __str__(self):
        return self.user.username

class PostJobs(models.Model):
    EXPERIENCE = [
        ('intern','Internship'),
        ('entry','Entry Level'),
        ('middle','Mid Level'),
        ('senior','Senior Level')
    ]
    description = models.TextField()
    job_location = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=10,choices=EXPERIENCE,default='entry')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    employer_profile  = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,related_name="jobs")

    def __str__(self):
        return self.employer_profile
