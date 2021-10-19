"""Defines URL patterns for aless_art_shop app"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from aless_art_shop.views import ProductListView, ProductDetailView, BlogListView, BlogPostView


app_name = "aless_art_shop"


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('gallery', ProductListView.as_view(), name='gallery'),
    path('gallery/detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('blogs', BlogListView.as_view(), name='blogs'),
    path('blogs/<slug:slug>/', BlogPostView.as_view(), name='blogdetail'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)