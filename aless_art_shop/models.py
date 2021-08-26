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

    # # photo = models.ImageField(upload_to="product_photo", blank=True)
    def __str__(self):
        return self.product_name
