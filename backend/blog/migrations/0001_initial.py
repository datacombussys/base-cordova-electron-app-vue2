# Generated by Django 2.1.12 on 2020-06-05 19:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datacom', '0001_initial'),
        ('employees', '0001_initial'),
        ('partners', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('blog_title_image', models.FileField(blank='True', upload_to='uploads')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
                ('datacom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datacom.Datacom')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
        ),
    ]