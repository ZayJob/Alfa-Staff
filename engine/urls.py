"""alfastaff URL Configuration."""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('alfastaff_account.urls')),
    path('', include('alfastaff_bonuses.urls')),
    path('', include('alfastaff_shedule.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
