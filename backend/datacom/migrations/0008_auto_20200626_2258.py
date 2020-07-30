# Generated by Django 3.0.7 on 2020-06-26 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouses', '0005_auto_20200626_2258'),
        ('salesoffices', '0008_auto_20200626_2258'),
        ('partners', '0007_auto_20200626_2258'),
        ('vendors', '0006_auto_20200626_2258'),
        ('commons', '0002_commonbarcode'),
        ('companies', '0008_auto_20200626_2258'),
        ('datacom', '0007_auto_20200626_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacom',
            name='barcode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='commons.CommonBarcode'),
        ),
        migrations.DeleteModel(
            name='CommonBarcode',
        ),
    ]