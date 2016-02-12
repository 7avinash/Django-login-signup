from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', LogIn, name = 'login'),
    url(r'^signup/', SignUp, name = 'signup'),
    url(r'^home/', Home, name = 'home'),
]
