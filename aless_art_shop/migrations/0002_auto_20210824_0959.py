# Generated by Django 3.1 on 2021-08-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aless_art_shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artwork',
            new_name='Listing',
        ),
    ]
