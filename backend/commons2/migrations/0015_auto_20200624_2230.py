# Generated by Django 3.0.7 on 2020-06-24 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons2', '0014_auto_20200623_0601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='archived',
            new_name='is_archived',
        ),
    ]
