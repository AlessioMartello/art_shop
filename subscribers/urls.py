"""Defines URL patterns for aless_art_shop app"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "subscribers"


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
]