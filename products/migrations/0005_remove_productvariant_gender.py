# Generated by Django 3.2.23 on 2023-12-15 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='gender',
        ),
    ]
