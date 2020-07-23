# Generated by Django 3.0.7 on 2020-07-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20200716_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='billing_address_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='primary_mailing_address_2',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='shipping_address_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
