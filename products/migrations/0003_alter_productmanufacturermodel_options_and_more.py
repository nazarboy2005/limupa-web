# Generated by Django 5.0.6 on 2024-05-27 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productcolormodel_productmanufacturermodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmanufacturermodel',
            options={'verbose_name': 'Manufacturer', 'verbose_name_plural': 'Manufacturers'},
        ),
        migrations.AlterModelOptions(
            name='productsizemodel',
            options={'verbose_name': 'Size', 'verbose_name_plural': 'Sizes'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='manufacturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.productmanufacturermodel'),
            preserve_default=False,
        ),
    ]
