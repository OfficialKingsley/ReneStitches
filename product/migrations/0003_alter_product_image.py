# Generated by Django 4.1 on 2022-09-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_category_options_alter_product_discount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="images/products/"),
        ),
    ]
