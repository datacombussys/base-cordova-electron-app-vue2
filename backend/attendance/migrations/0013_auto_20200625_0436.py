# Generated by Django 3.0.7 on 2020-06-25 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_remove_leaverequest_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaverequest',
            options={},
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='date_added',
        ),
    ]
