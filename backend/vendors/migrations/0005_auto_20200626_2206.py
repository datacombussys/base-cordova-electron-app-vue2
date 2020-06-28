# Generated by Django 3.0.7 on 2020-06-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_auto_20200626_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='is_salesoffice',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_warehouse',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
