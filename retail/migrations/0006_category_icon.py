# Generated by Django 5.0.6 on 2024-12-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retail", "0005_product_discounted_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="retail/categories/icons/"
            ),
        ),
    ]
