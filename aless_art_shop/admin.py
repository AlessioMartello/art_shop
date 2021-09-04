from django.contrib import admin

from .models import Catalogue, Product, Donation


class DonationAdminSite(admin.AdminSite):
    site_header = "Donation admin"
    site_title = "Donation Portal"
    index_title = "Welcome to the Donations admin"


donation_admin_site = DonationAdminSite(name='doantion_admin')

admin.site.register(Catalogue)
admin.site.register(Product)
donation_admin_site.register(Donation)
