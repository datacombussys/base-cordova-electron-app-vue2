# Generated by Django 2.1.12 on 2020-06-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invcategory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='invcategoryclass',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='inventorybarcode',
            name='barcode_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventorybarcode',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventorybarcode',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryimage',
            name='sub_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryimage',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryimage',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventorylabels',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='inventorylabels',
            name='json_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventorylabels',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
