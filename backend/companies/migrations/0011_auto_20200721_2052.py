# Generated by Django 3.0.7 on 2020-07-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_auto_20200718_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='primary_mailing_address_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
