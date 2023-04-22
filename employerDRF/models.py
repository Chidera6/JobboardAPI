from django.db import models
from django.contrib.auth.models import AbstractUser,User

class CustomUser(AbstractUser):
    "A custom user models for all the users"
    USER_TYPE_CHOICES = ("1","Admin"),("2","Employer"),("3","Applicant")
    user_type = models.PositiveIntegerField(default="3",null=True,choices=USER_TYPE_CHOICES)
    def __str__(self):
        return self.username
  
   
class EmployerProfile(models.Model):
    Industry = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    description = models.TextField()
    telephone = models.PositiveIntegerField(null=True)
    logo = models.ImageField(null=True,upload_to='images/users',blank=True) 
    social_media = models.CharField(max_length=255)
    company_name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    date_created = models.DateField(auto_now_add=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="profile")
    
    def __str__(self):
        return self.user.username

class Jobs(models.Model):
    EXPERIENCE = [
        ('intern','Internship'),
        ('entry','Entry Level'),
        ('middle','Mid Level'),
        ('senior','Senior Level')
    ]
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_location = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=10,choices=EXPERIENCE,default='entry')
    job_requirements = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    application_deadline = models.DateField()
    employer_profile  = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,related_name="jobs")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title
