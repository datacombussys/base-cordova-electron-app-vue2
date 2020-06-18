# Generated by Django 3.0.7 on 2020-06-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_salestax_enable_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salestax',
            name='filing_frequency',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Yearly', 'Yearly')], default='Quarterly', max_length=100),
        ),
    ]
