from django.contrib import admin
from .models import *

#    list_display = ('id',"first_name","last_name","email")

admin.site.register(EmployerProfile)
admin.site.register(PostJobs)
admin.site.register(CustomUser)