# Generated by Django 3.0.7 on 2020-06-25 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('employees', '0005_employee_is_sales_office_ee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='modules_managed',
            field=models.ManyToManyField(blank=True, null=True, to='contenttypes.ContentType'),
        ),
    ]
