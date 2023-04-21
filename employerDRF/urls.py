from django.urls import path
from . import views
urlpatterns = [
     path("employer-profiles",views.EmployerProfileView.as_view()),
     path("employer-profiles/<int:pk>",views.EmployerProfileSingleView.as_view()),
     path("jobs",views.PostJobView.as_view()),
     path("jobs/<int:pk>",views.PostJobSingleView.as_view()),
]