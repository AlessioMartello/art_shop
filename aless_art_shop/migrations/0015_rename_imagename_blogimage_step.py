# Generated by Django 3.2.6 on 2021-10-25 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aless_art_shop', '0014_rename_blogpost_blogimage_postname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogimage',
            old_name='imageName',
            new_name='step',
        ),
    ]
