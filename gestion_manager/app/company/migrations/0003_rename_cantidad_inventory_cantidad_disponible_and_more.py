# Generated by Django 5.1.1 on 2024-09-07 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_inventory_product_delete_company_inventory_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='cantidad',
            new_name='cantidad_disponible',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='producto',
            new_name='product',
        ),
    ]
