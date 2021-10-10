"""art_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from aless_art_shop.admin import donation_admin_site

from aless_art_shop.sitemaps import StaticViewSitemap, ProductSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'donation_admin/', donation_admin_site.urls),
    path(r'', include('aless_art_shop.urls', namespace='aless_art_shop')),
    path(r'stripe_payments/', include('stripe_payments.urls', namespace='stripe_payments')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
