# Generated by Django 2.1.12 on 2020-06-05 19:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datacom', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
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
        migrations.CreateModel(
            name='CardProcessingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('processor_name', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('merchant_id', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,15}$')])),
                ('pin', models.CharField(blank=True, max_length=64, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('name_on_card', models.CharField(max_length=255)),
                ('card_number_token', models.CharField(blank=True, max_length=255, null=True)),
                ('card_cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=255)),
                ('billing_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=50, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_zip', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,5}$')])),
                ('card_exp_date', models.DateField(blank=True, null=True)),
                ('card_exp_month', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,2}$')])),
                ('card_exp_year', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('last4', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('is_primary', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_debit', models.BooleanField(default=True)),
                ('card_type', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ElavonCCRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('ssl_merchant_id', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,15}$')])),
                ('ssl_user_id', models.CharField(blank=True, max_length=15, null=True)),
                ('ssl_pin', models.CharField(blank=True, max_length=64, null=True)),
                ('ssl_transaction_type', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_card_number', models.CharField(blank=True, max_length=18, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,18}$')])),
                ('ssl_exp_date', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('ssl_card_present', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_track_data', models.CharField(blank=True, max_length=76, null=True)),
                ('ssl_enc_track_data', models.CharField(blank=True, max_length=160, null=True)),
                ('ssl_enc_track_data_format', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_encrypted_track1_data', models.CharField(blank=True, max_length=160, null=True)),
                ('ssl_encrypted_track2_data', models.CharField(blank=True, max_length=160, null=True)),
                ('ssl_ksn', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_vm_mobile_source', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_vendor_id', models.CharField(blank=True, max_length=50, null=True)),
                ('ssl_mobile_id', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_token', models.CharField(blank=True, max_length=2, null=True)),
                ('ssl_pos_mode', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,2}$')])),
                ('ssl_entry_mode', models.CharField(blank=True, max_length=2, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,2}$')])),
                ('ssl_dynamic_dba', models.CharField(blank=True, max_length=21, null=True)),
                ('ssl_get_token', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_add_token', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_tip_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_server', models.CharField(blank=True, max_length=8, null=True)),
                ('ssl_shift', models.CharField(blank=True, max_length=4, null=True)),
                ('ssl_cvv2cvc2', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('ssl_cvv2cvc2_indicator', models.CharField(blank=True, max_length=1, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,1}$')])),
                ('ssl_customer_code', models.CharField(blank=True, max_length=17, null=True)),
                ('ssl_salestax', models.CharField(blank=True, max_length=8, null=True)),
                ('ssl_salestax_indicator', models.CharField(blank=True, max_length=2, null=True)),
                ('ssl_invoice_number', models.CharField(blank=True, max_length=25, null=True)),
                ('ssl_transaction_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('ssl_recurring_flag', models.CharField(blank=True, max_length=1, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,1}$')])),
                ('ssl_payment_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,15}$')])),
                ('ssl_payment_count', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('ssl_departure_Date', models.CharField(blank=True, max_length=10, null=True)),
                ('ssl_completion_Date', models.CharField(blank=True, max_length=10, null=True)),
                ('ssl_merchant_initiated_unscheduled', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_oar_data', models.CharField(blank=True, max_length=60, null=True)),
                ('ssl_ps2000_data', models.CharField(blank=True, max_length=22, null=True)),
                ('ssl_level3_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_ship_to_zip', models.CharField(blank=True, max_length=9, null=True)),
                ('ssl_ship_to_country', models.CharField(blank=True, max_length=3, null=True)),
                ('ssl_shipping_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_ship_from_postal_code', models.CharField(blank=True, max_length=9, null=True)),
                ('ssl_discount_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_duty_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_national_tax_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_national_tax_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_order_date', models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')])),
                ('ssl_other_tax', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_summary_commodity_code', models.CharField(blank=True, max_length=4, null=True)),
                ('ssl_merchant_vat_number', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_customer_vat_number', models.CharField(blank=True, max_length=13, null=True)),
                ('ssl_freight_tax_amount', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_vat_invoice_number', models.CharField(blank=True, max_length=15, null=True)),
                ('ssl_tracking_number', models.CharField(blank=True, max_length=25, null=True)),
                ('ssl_shipping_company', models.CharField(blank=True, max_length=50, null=True)),
                ('ssl_other_fees', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_line_item_description', models.CharField(blank=True, max_length=35, null=True)),
                ('ssl_line_Item_product_code', models.CharField(blank=True, max_length=13, null=True)),
                ('ssl_line_Item_commodity_code', models.CharField(blank=True, max_length=12, null=True)),
                ('ssl_line_Item_quantity', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_line_Item_unit_of_measure', models.CharField(blank=True, max_length=3, null=True)),
                ('ssl_line_Item_unit_cost', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_line_Item_discount_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_line_Item_tax_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_line_item_discount_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_line_Item_tax_rate', models.CharField(blank=True, max_length=4, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,4}$')])),
                ('ssl_line_Item_tax_amount', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_line_Item_tax_type', models.CharField(blank=True, max_length=4, null=True)),
                ('ssl_line_Item_extended_total', models.CharField(blank=True, max_length=9, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,9}$')])),
                ('ssl_line_Item_total', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_line_Item_alternative_tax', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('ssl_eci_ind', models.CharField(blank=True, max_length=1, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,1}$')])),
                ('ssl_3dsecure_value', models.CharField(blank=True, max_length=80, null=True)),
                ('ssl_xid', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_eWallet', models.CharField(blank=True, max_length=10, null=True)),
                ('ssl_callback_url', models.CharField(blank=True, max_length=200, null=True)),
                ('ssl_eWallet_shipping', models.CharField(blank=True, max_length=1, null=True)),
                ('ssl_product_string', models.CharField(blank=True, max_length=200, null=True)),
                ('ssl_transaction_source', models.CharField(blank=True, max_length=20, null=True)),
                ('ssl_applepay_web', models.TextField(blank=True, null=True)),
                ('ssl_applepay_billing', models.TextField(blank=True, null=True)),
                ('ssl_applepay_shipping', models.TextField(blank=True, null=True)),
                ('ssl_visapayload', models.TextField(blank=True, null=True)),
                ('ssl_avs_address', models.CharField(blank=True, max_length=30, null=True)),
                ('ssl_avs_zip', models.CharField(blank=True, max_length=9, null=True)),
                ('ssl_description', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_partial_auth_indicator', models.CharField(blank=True, max_length=1, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,1}$')])),
                ('ssl_healthcare_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_otc_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_prescription_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_clinic_other_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_dental_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_vision_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('ssl_transit_amount', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,11}$')])),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ElavonCCResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('ssl_result', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_result_message', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_txn_id', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_txn_time', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_approval_code', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_card_number', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_card_short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_card_type', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_promo_list', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_token', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_token_response', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_add_token_response', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_base_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_tip_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_server', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_shift', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_avs_response', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_cvv2_response', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_invoice_number', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_transaction_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_txn_currency_code', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_markup', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_conversion_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_cardholder_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_cardholder_currency', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_cardholder_base_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_cardholder_tip_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_requested_amount', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_balance_due', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_account_balance', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_oar_data', models.CharField(blank=True, max_length=255, null=True)),
                ('ssl_ps2000_data', models.CharField(blank=True, max_length=255, null=True)),
                ('errorCode', models.CharField(blank=True, max_length=255, null=True)),
                ('errorMessage', models.CharField(blank=True, max_length=255, null=True)),
                ('errorName', models.CharField(blank=True, max_length=255, null=True)),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vthpp.ElavonCCRequest')),
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
    ]