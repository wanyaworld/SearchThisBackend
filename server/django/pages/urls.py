from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('document', documentPageView, name='document'),
]
