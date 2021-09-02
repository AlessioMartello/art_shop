from django.shortcuts import render
from .models import Catalogue, Product


def index(request):
    """The home page for aless_art_shop"""
    return render(request, "aless_art_shop/index.html")


def product(request, product_id):
    """Display the individual listing details"""
    catalogue = Catalogue.objects.get(product_id)
    product = Product.objects.all()
    context = {'catalogue': catalogue, 'product': product}
    return render(request, 'aless_art_shop/product_list.html', context)

def about(request):
    """Display the about page"""
    return render(request, 'aless_art_shop/about.html')