from django.contrib import admin

from .models import Catalogue, Product, Donation, BlogPost


class DonationAdminSite(admin.AdminSite):
    site_header = "Donation admin"
    site_title = "Donation Portal"
    index_title = "Welcome to the Donations admin"


donation_admin_site = DonationAdminSite(name='donation_admin')

admin.site.register(Catalogue)
admin.site.register(Product)
admin.site.register(BlogPost)
donation_admin_site.register(Donation)
