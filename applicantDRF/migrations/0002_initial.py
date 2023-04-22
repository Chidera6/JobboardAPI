# Generated by Django 4.1.7 on 2023-04-22 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employerDRF', '0001_initial'),
        ('applicantDRF', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantprofile',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employerDRF.postjobs'),
        ),
        migrations.AddField(
            model_name='applicantprofile',
            name='skills',
            field=models.ManyToManyField(to='applicantDRF.skill'),
        ),
        migrations.AddField(
            model_name='applicantprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]