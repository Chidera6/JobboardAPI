from django.db import models
from employerDRF.models import CustomUser

class Skill(models.Model):
    name = models.CharField(max_length=255)


class ApplicantProfile(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    telephone = models.PositiveIntegerField(null=True)
    years_of_experience = models.PositiveIntegerField()
    education = models.CharField(max_length=500)
    certification = models.ImageField(upload_to='images/certificates',null=True,blank=True)
    avatar = models.ImageField(upload_to='images/users',null=True,blank=True)
    cover_letter = models.FileField(upload_to='images/files',null=True,blank=True)
    cv = models.FileField(upload_to='images/files',null=True,blank=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)

    

    def __str__(self) -> str:
        return self.skills
    


    
    """
    cover_image = ProcessedImageField(
        verbose_name=_('Cover'),
        blank=False,
        null=False,
        format='JPEG',
        options={'quality': 90},
        processors=[ResizeToFill(600, 200)],
        upload_to=cover_image_directory)
        """
    
"""
class Applicant(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)

class Skill(models.Model):
    name = models.CharField(max_length=255)
"""

#applicants = Applicant.objects.filter(skills__name__in=['Python', 'JavaScript'])
