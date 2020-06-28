# Generated by Django 3.0.7 on 2020-06-28 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200625_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorybarcode',
            name='product',
        ),
        migrations.AddField(
            model_name='inventory',
            name='barcode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.InventoryBarcode'),
        ),
    ]
