"""This module contain urls for application."""

from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *


name_apps = 'alfastaff_account'


urlpatterns = [
    path('', login_user, name='login'),
    path('login', login_user, name='login'),
    path('signup', signup_user, name='signup'),
    path('signup_insert', signup_user_insert, name='signup_insert'),
    path('reset', reset_password, name='reset'),
    path('reset_insert', reset_password_insert, name='reset_insert'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_user,
        name='activate'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
