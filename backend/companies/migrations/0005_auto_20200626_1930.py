# Generated by Django 3.0.7 on 2020-06-26 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_company_company_docs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='billing_contact_list',
            new_name='billing_contacts',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='primary_contact_list',
            new_name='primary_contacts',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='shipping_contact_list',
            new_name='shipping_contacts',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='technical_contact_list',
            new_name='technical_contacts',
        ),
    ]