"""Defines URL patterns for aless_art_shop app"""

from django.urls import path

from . import views

app_name = "aless_art_shop"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Detailed page for a single listing
    path('product/<int:id>/', views.product, name='product'),
    # About page
    path('about/', views.about, name="about")
]