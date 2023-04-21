from django.urls import path
from . import views 

urlpatterns = [
    path("applicant-profiles",views.ApplicantProfileView.as_view()),
    path("applicant-profiles/<int:pk>",views.ApplicantProfileSingleView.as_view())
]