from django.db import models


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
    def __str__(self):
        return self.product_name


class Donation(models.Model):
    """An group of donations the user can choose"""
    amount = models.IntegerField(primary_key=True)
    stripe_price_id = models.CharField(max_length=100)

    def __int__(self):
        return self.amount