# Generated by Django 3.0.7 on 2020-07-16 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesoffices', '0008_auto_20200626_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesoffice',
            name='acct_closure_date',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='corp_address',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='corp_city',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='corp_state',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='corp_zip',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='main_email',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='main_fax',
        ),
        migrations.RemoveField(
            model_name='salesoffice',
            name='main_phone',
        ),
    ]