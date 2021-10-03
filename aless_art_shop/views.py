from django.shortcuts import render
from django.views.generic import ListView, DetailView
from aless_art_shop.models import Product
from django.conf import settings


def index(request):
    """The home page for artlessi.co.uk"""
    return render(request, "aless_art_shop/index.html")


def about(request):
    """Display the about page"""
    return render(request, 'aless_art_shop/about.html')


def faqs(request):
    """Display the faqs page"""
    return render(request, 'aless_art_shop/faqs.html')


class ProductListView(ListView):
    model = Product
    template_name = "aless_art_shop/product_list.html"
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = "aless_art_shop/product_detail.html"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['stripe_public_key'] = settings.STRIPE_PUBLIC_KEY
        return context
