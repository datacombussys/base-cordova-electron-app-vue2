# Generated by Django 3.0.7 on 2020-06-25 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('humanresources', '0003_auto_20200625_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mileagereimbursement',
            name='read',
        ),
    ]
