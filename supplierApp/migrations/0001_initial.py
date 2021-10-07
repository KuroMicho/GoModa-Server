# Generated by Django 3.2.8 on 2021-10-06 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('address', models.CharField(max_length=30, verbose_name='Address')),
                ('city', models.CharField(max_length=20, verbose_name='City')),
            ],
        ),
    ]
