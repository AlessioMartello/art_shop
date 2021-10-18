from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from aless_art_shop.urls import app_name as art_shop_app
from stripe_payments.urls import app_name as stripe_app
from aless_art_shop.models import Product, BlogPost


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "monthly"

    def items(self):
        return [f'{art_shop_app}:index', f'{art_shop_app}:about', f'{art_shop_app}:faqs', f'{stripe_app}:donate']

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_on


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def location(self, obj):
        return f'/blogs/{obj.slug}/'

    def lastmod(self, obj):
        return obj.updated_on
