# Generated by Django 3.0.7 on 2020-07-16 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_auto_20200626_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='acct_closure_date',
            new_name='closure_date',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='corp_address',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='corp_city',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='corp_state',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='corp_zip',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='main_email',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='main_fax',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='main_phone',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='status',
        ),
    ]
