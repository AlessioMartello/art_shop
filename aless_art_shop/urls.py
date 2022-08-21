"""Defines URL patterns for aless_art_shop app"""

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from aless_art_shop.views import ProductListView, ProductDetailView, BlogListView, BlogPostView, TagIndexiew


app_name = "aless_art_shop"


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('faqs/', views.faqs, name="faqs"),
    path('gallery', ProductListView.as_view(), name='gallery'),
    path('gallery/detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('blogs', BlogListView.as_view(), name='blogs'),
    path('blogs/<slug:slug>/', BlogPostView.as_view(), name='blogdetail'),
    path('blogs/tags/<slug:tag_slug>/', TagIndexiew.as_view(), name='posts_by_tag'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)