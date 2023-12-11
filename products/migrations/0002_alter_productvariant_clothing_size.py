# Generated by Django 3.2.23 on 2023-12-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='clothing_size',
            field=models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large'), ('3XL', 'Triple Extra Large')], max_length=10, null=True),
        ),
    ]