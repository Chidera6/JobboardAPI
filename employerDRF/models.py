from django.db import models

# Create your models here.
class EmployerProfile(models.Model):
    name = models.CharField(max_length=200)
    #surname = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    telephone = models.PositiveIntegerField()
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class PostJobs(models.Model):
    EXPERIENCE = [
        ('intern','Internship'),
        ('entry','Entry Level'),
        ('middle','Mid Level'),
        ('seniour','Senior Level')
    ]
    description = models.TextField()
    job_location = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=10,choices=EXPERIENCE,default='entry')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    employer_profile  = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)

    