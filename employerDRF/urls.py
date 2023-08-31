from django.urls import path
from . import views
app_name = "employer"
urlpatterns = [
     path("employer-profiles/create",views.EmployerProfileCreateView.as_view()),
     path("employer-profiles/list",views.EmployerProfilesListView.as_view()),
     path("employer-profile/<str:user__username>",views.EmployerProfileSingleView.as_view(),name='employer_detail'),
     path("jobs/create",views.JobCreateView.as_view()),
     path("jobs/list",views.JobListView.as_view()),
     path("job/<slug:slug>",views.JobSingleView.as_view(),name='job_detail'),
     
]