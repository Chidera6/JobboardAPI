from django.db import models
from employerDRF.models import CustomUser,Jobs
from django.urls import reverse
from django.utils.text import slugify

class ApplicantProfile(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    contact_phone = models.PositiveIntegerField(null=True)
    years_of_experience = models.PositiveIntegerField()
    education = models.CharField(max_length=500)
    certification = models.ImageField(upload_to='images/certificates',null=True,blank=True)
    avatar = models.ImageField(upload_to='images/users',null=True,blank=True)
    cover_letter = models.FileField(upload_to='images/files',null=True,blank=True)
    cv = models.FileField(upload_to='images/files',null=True,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return self.user.username
    

class Application(models.Model):
    jobs = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    applicant_profile = models.ForeignKey(ApplicantProfile,on_delete=models.CASCADE)

    
   
    
