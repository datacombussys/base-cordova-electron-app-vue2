# Generated by Django 3.0.7 on 2020-06-25 03:05

from django.db import migrations, models
import django.db.models.deletion
import eventtools.models


class Migration(migrations.Migration):

    dependencies = [
        ('datacom', '0005_datacom_company_docs'),
        ('companies', '0004_company_company_docs'),
        ('partners', '0004_partner_company_docs'),
        ('employees', '0002_auto_20200625_0056'),
        ('attendance', '0010_auto_20200619_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaverequest',
            old_name='leave_comments',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='approve_decline_date',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='approved_by',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='files',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='leaveType',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='personal_remaining',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='pto_remaining',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='sick_remaining',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='vacation_remaining',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='disposition_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='employees/leave-docs'),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='leave_type',
            field=models.CharField(blank=True, choices=[('Vacation', 'Vacation'), ('Sick', 'Sick'), ('Personal', 'Personal'), ('Medical', 'Medical'), ('Paid Time Off', 'Paid Time Off')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='read',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Declined', 'Declined'), ('Open', 'Open'), ('Expired', 'Expired'), ('Deleted', 'Deleted')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='PayCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('frequency', models.CharField(blank=True, max_length=100, null=True)),
                ('rule', models.CharField(blank=True, max_length=250, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('employees', models.ManyToManyField(blank=True, to='employees.Employee')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, eventtools.models.OccurrenceMixin),
        ),
        migrations.AlterField(
            model_name='paycyclerecurrence',
            name='recurrence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.PayCycle'),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='cycle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.PayCycle'),
        ),
        migrations.DeleteModel(
            name='PayCycles',
        ),
    ]