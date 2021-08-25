from django.db import models


class Catalogue(models.Model):
    """A piece of art the user can purchase"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)  # The maxlength may need increasing

    def __str__(self):
        return self.name


class Product(models.Model):
    """One product a user can view and buy"""
    title = models.CharField(max_length=255, default='SOME STRING')
    product = models.OneToOneField(
        Catalogue, on_delete=models.CASCADE, related_name="products", default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # photo = models.ImageField(upload_to="product_photo", blank=True)
