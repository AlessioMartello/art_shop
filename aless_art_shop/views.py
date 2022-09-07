from django.shortcuts import render
from django.views.generic import ListView, DetailView
from aless_art_shop.models import Product, BlogPost, BlogImage
from django.conf import settings
from taggit.models import Tag
from django.http import HttpResponse
from django.views import View


def index(request):
    """The home page for artlessi.co.uk"""
    blogs = BlogPost.objects.order_by('-created_on')
    context = {'blogs': blogs}
    return render(request, "aless_art_shop/index.html", context)


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


class TaxMixIn(object):
    def get_context_data(self, **kwargs):
        context = super(TaxMixIn, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class BlogListView(TaxMixIn, ListView):
    queryset = BlogPost.objects.order_by('-created_on')
    template_name = "aless_art_shop/blog_list.html"


class BlogPostView(DetailView):
    model = BlogPost
    template_name = "aless_art_shop/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        context["blogs"] = BlogPost.objects.all()
        context["walkthrough_steps"] = BlogImage.objects.filter(postname=self.object)
        return context


class TagIndexiew(TaxMixIn, ListView):
    model = BlogPost
    template_name = "aless_art_shop/blog_list.html"

    def get_queryset(self):
        return BlogPost.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


class AdsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("google.com, pub-1268104295070057, DIRECT, f08c47fec0942fa0")
