# Generated by Django 3.0.7 on 2021-02-12 20:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
        ('datacom', '0001_initial'),
        ('companies', '0001_initial'),
        ('vendors', '0001_initial'),
        ('commons', '0001_initial'),
        ('warehouses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvCategoryClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('global_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('model_number', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='inventory/profile')),
                ('gallery_imgs', models.TextField(blank=True, null=True)),
                ('is_service', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_tracked', models.BooleanField(default=False)),
                ('is_downloadable', models.BooleanField(default=False)),
                ('is_on_website', models.BooleanField(default=False)),
                ('is_on_sale', models.BooleanField(default=False)),
                ('is_taxable', models.BooleanField(default=False)),
                ('product_id', models.CharField(blank=True, max_length=20, null=True)),
                ('product_type', models.CharField(blank=True, max_length=100, null=True)),
                ('initial_qty', models.IntegerField(blank=True, null=True)),
                ('sales_notes', models.TextField(blank=True, null=True)),
                ('vendor_notes', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('msrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('online_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('purchase_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('wholesale_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('sale_expire_date', models.DateField(blank=True, null=True)),
                ('income_acct', models.CharField(blank=True, max_length=50, null=True)),
                ('expense_acct', models.CharField(blank=True, max_length=50, null=True)),
                ('retail_margin', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('wholesale_margin', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('qty_on_hand', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('reorder_level', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='inventory/files')),
            ],
            options={
                'ordering': ['name', 'date_added'],
            },
        ),
        migrations.CreateModel(
            name='InventoryBarcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('barcode_number', models.CharField(max_length=8)),
                ('upc', models.CharField(max_length=8)),
                ('ean', models.CharField(max_length=8)),
                ('custom_sku', models.CharField(max_length=8)),
                ('manu_sku', models.CharField(max_length=8)),
                ('barcode_type', models.CharField(blank=True, max_length=10, null=True)),
                ('is_sku', models.BooleanField(default=False)),
                ('is_upc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLabels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('json_data', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='inventory/gallery')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='barcode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.InventoryBarcode'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.InvCategory'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='datacom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='uom_dimensions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='commons.UOMDimensions'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='uom_weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='commons.UOMWeight'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vendors.Vendor'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouse_loc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='warehouses.Warehouse'),
        ),
    ]
