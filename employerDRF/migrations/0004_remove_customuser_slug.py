# Generated by Django 4.1.7 on 2023-05-17 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employerDRF', '0003_alter_jobs_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='slug',
        ),
    ]