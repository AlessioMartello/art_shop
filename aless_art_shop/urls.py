"""Defines URL patterns for aless_art_shop app"""

from django.urls import path

from . import views

app_name = "aless_art_shop"
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id>/', views.product, name='product'),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs")
]