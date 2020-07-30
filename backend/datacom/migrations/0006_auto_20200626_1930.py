# Generated by Django 3.0.7 on 2020-06-26 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datacom', '0005_datacom_company_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacom',
            name='billing_contacts',
            field=models.ManyToManyField(blank=True, related_name='datacom_billing_contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='datacom',
            name='primary_contacts',
            field=models.ManyToManyField(blank=True, related_name='datacom_primary_contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='datacom',
            name='shipping_contacts',
            field=models.ManyToManyField(blank=True, related_name='datacom_shipping_contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='datacom',
            name='technical_contacts',
            field=models.ManyToManyField(blank=True, related_name='datacom_technical_contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]