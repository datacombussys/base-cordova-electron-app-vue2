# Generated by Django 2.1.12 on 2020-06-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='billing_country',
            field=models.CharField(default='USA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='primary_mailing_country',
            field=models.CharField(default='USA', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='shipping_country',
            field=models.CharField(default='USa', max_length=200),
            preserve_default=False,
        ),
    ]