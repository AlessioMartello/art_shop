# Generated by Django 3.2.6 on 2021-08-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aless_art_shop', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_price_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
