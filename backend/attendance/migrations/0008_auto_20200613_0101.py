# Generated by Django 3.0.7 on 2020-06-13 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_auto_20200612_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancesettings',
            name='operating_hours',
            field=models.ManyToManyField(blank=True, to='attendance.BusinessOperatingHours'),
        ),
    ]