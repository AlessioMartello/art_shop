from django.shortcuts import render
from .models import Catalogue, Product


def index(request):
    """The home page for aless_art_shop"""
    return render(request, "aless_art_shop/index.html")


def catalogue(request):
    """Display the listings"""
    catalogue = Catalogue.objects.order_by('name')
    product = Product.objects.all()
    context = {'catalogue': catalogue, 'product':product}
    return render(request, 'aless_art_shop/catalogue.html', context)


def product(request, id):
    """Display the individual listing details"""
    product = Product.objects.filter(id=id)
    context = {'product': product}
    return render(request, 'aless_art_shop/product.html', context)
