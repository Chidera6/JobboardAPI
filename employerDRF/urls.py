from django.urls import path
from . import views
urlpatterns = [
     path("employer-profiles/create",views.EmployerProfileCreateView.as_view()),
     path("employer-profiles/list",views.EmployerProfilesListView.as_view()),
     path("employer-profile/<int:pk>",views.EmployerProfileSingleView.as_view()),
     path("jobs/create",views.JobCreateView.as_view()),
     path("jobs/list",views.JobListView.as_view()),
     path("job/<int:pk>",views.JobSingleView.as_view()),
     
]