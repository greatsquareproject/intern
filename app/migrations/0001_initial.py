# Generated by Django 4.2.2 on 2023-08-28 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('purchase_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=500)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Companyname', models.CharField(default='Yogaa Infrastructure Ptv Ltd,.', max_length=250)),
                ('address', models.CharField(default='521-3-1, 1, 1/521-3-1, 8th St, Poriyalar Nagar, Tiruppalai, Madurai, Tamil Nadu 625014', max_length=150)),
                ('phone', models.IntegerField(default='+91 9900809781')),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
