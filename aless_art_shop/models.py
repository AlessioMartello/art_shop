from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Catalogue(models.Model):
    """An group of products the user can inspect"""
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=2000)  # The max_length may need increasing

    def __str__(self):
        return self.name


class Product(models.Model):
    """A product a user can view and buy, associated with a catalogue"""
    product_name = models.CharField(max_length=255)
    catalogue = models.ForeignKey(
        Catalogue, on_delete=models.CASCADE, related_name="art_name")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_price_id = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, default="Enter product description here")
    photo = models.ImageField(upload_to="images/", blank=True)
    size = models.CharField(max_length=50)
    material = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('aless_art_shop:detail', args=[str(self.id)])


class Donation(models.Model):
    """An group of donations the user can choose"""
    amount = models.IntegerField(primary_key=True)
    stripe_price_id = models.CharField(max_length=100)

    def __int__(self):
        return self.amount


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    sub_heading = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    #content = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blog_photo = models.ImageField(upload_to="images/", blank=True)
    video_embed_url = models.TextField(blank=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    step = models.TextField(blank=True)
    postname = models.ForeignKey(BlogPost, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to="images/", blank=True)