# Generated by Django 3.2.23 on 2023-12-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20231214_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('women', 'women'), ('kids', 'kids')], max_length=10, null=True),
        ),
    ]
