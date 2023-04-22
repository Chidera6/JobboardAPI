from django.urls import path
from . import views 

urlpatterns = [
    path("applicant-profiles/create",views.ApplicantProfileView.as_view()),
    path("applicant-profiles/list",views.ApplicantProfileListView.as_view()),
    path("applicant-profile/<int:pk>",views.ApplicantProfileSingleView.as_view()),
    path("job/<int:pk>/apply/create",views.Applications.as_view()),
    path("job/<int:pk>/list",views.ApplicationsListView.as_view()),
    path("job/<int:pk/applications/<int:pk",views.ApplicationsSingleView.as_view()),
]