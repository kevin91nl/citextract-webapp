"""CiteXtract URL Configuration."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('cms.urls'))
]
