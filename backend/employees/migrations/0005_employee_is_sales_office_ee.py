# Generated by Django 3.0.7 on 2020-06-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_is_module_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_sales_office_ee',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
