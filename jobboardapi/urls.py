from django.contrib import admin
from django.urls import path,include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Job Board API",
      default_version='v1',
      description="Job Board API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

"""
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MTk5NjkyMywianRpIjoiZjZiNjc5MjhjNTRjNGM0ZjkyMjU4MjFkYzQ5NTllZjUiLCJ1c2VyX2lkIjoxfQ.P5OkgzaijKfivUH1zghjyLvrJ-kNmrf7M4E1pTGSYQk",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxOTEwODIzLCJqdGkiOiJkZTNkOGY3ZDc1M2Q0NGI4OTlmNjAzZGU3ZTcyOGIwZCIsInVzZXJfaWQiOjF9.5ALFnL0Ui8oGDivVgNawTXxSbxENhEOLrF3eStioV8I"
}
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('applicantDRF.urls')),
    path('api/v1/',include('employerDRF.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)