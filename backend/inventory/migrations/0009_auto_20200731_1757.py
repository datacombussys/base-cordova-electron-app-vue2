# Generated by Django 3.0.7 on 2020-07-31 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200731_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='product_desc',
            new_name='description',
        ),
    ]
