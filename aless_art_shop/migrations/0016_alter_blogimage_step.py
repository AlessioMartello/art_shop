# Generated by Django 3.2.6 on 2021-10-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aless_art_shop', '0015_rename_imagename_blogimage_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='step',
            field=models.TextField(blank=True),
        ),
    ]
