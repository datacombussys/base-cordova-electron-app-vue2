# Generated by Django 3.0.7 on 2021-02-12 20:13

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datacom', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('name_on_card', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=255)),
                ('card_number_token', models.CharField(blank=True, max_length=255, null=True)),
                ('processor_token', models.CharField(blank=True, max_length=255, null=True)),
                ('card_cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_zip', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,5}$')])),
                ('billing_country', models.CharField(blank=True, max_length=200, null=True)),
                ('card_exp_date', models.DateField(blank=True, null=True)),
                ('card_exp_month', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,2}$')])),
                ('card_exp_year', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('last4', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('is_primary', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_debit', models.BooleanField(default=True)),
                ('card_type', models.CharField(blank=True, max_length=100, null=True)),
                ('card_brand', models.CharField(blank=True, choices=[('VS', 'VISA'), ('MC', 'MasterCard'), ('DS', 'Discover'), ('DC', 'Dincer Club'), ('AM', 'American Express')], max_length=2, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForteACHResponseCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='ForteACHReturnCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='ForteACHSettlementCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('description', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='ForteACHStatusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('txn_id', models.CharField(blank=True, max_length=255, null=True)),
                ('result', models.CharField(blank=True, max_length=2, null=True)),
                ('approval_code', models.CharField(blank=True, max_length=255, null=True)),
                ('errorCode', models.IntegerField(blank=True, null=True)),
                ('errorMessage', models.CharField(blank=True, max_length=255, null=True)),
                ('errorName', models.CharField(blank=True, max_length=255, null=True)),
                ('jsonRequest', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('jsonResult', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('success', models.BooleanField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('credit_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.CreditCard')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='ForteACHTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('response_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.ForteACHResponseCode')),
                ('return_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.ForteACHReturnCode')),
                ('settlement_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.ForteACHSettlementCode')),
                ('status_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.ForteACHStatusCode')),
            ],
        ),
        migrations.CreateModel(
            name='CardProcessingAPIKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('processor_name', models.CharField(choices=[('Elavon', 'Elavon'), ('Forte', 'Forte')], max_length=20)),
                ('merchant_id', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{1,20}$')])),
                ('pin', models.CharField(blank=True, max_length=64, null=True)),
                ('ssl_user_id', models.CharField(blank=True, max_length=15, null=True)),
                ('is_demo', models.BooleanField(blank=True, default=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('result', models.CharField(blank=True, max_length=2, null=True)),
                ('result_message', models.CharField(blank=True, max_length=255, null=True)),
                ('approval_code', models.CharField(blank=True, max_length=255, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('token_response', models.CharField(blank=True, max_length=255, null=True)),
                ('add_token_response', models.CharField(blank=True, max_length=255, null=True)),
                ('errorCode', models.IntegerField(blank=True, null=True)),
                ('errorMessage', models.CharField(blank=True, max_length=255, null=True)),
                ('errorName', models.CharField(blank=True, max_length=255, null=True)),
                ('jsonRequest', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('jsonResult', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('credit_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vthpp.CreditCard')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='ACHAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('name_on_account', models.CharField(max_length=255)),
                ('account_number_token', models.CharField(blank=True, max_length=255, null=True)),
                ('routing_number', models.CharField(max_length=9)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_zip', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,5}$')])),
                ('last4', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('is_primary', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_business_acct', models.BooleanField(default=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
