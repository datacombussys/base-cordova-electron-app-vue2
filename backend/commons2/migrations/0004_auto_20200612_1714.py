# Generated by Django 2.1.12 on 2020-06-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons2', '0003_auto_20200612_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]