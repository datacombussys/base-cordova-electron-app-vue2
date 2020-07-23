# Generated by Django 3.0.7 on 2020-07-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_auto_20200716_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='billing_address_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='primary_mailing_address_2',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='shipping_address_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
