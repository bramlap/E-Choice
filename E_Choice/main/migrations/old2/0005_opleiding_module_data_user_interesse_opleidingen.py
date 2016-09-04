# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opleiding_module_data',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('opleiding', models.CharField(default='Opleiding', max_length=35)),
                ('module', models.CharField(default='module', max_length=35)),
                ('date1', models.CharField(default='date1', max_length=35)),
                ('date2', models.CharField(default='date2', max_length=35)),
                ('date3', models.CharField(default='date3', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='User_Interesse_Opleidingen',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(default='User', max_length=35)),
                ('naam_opleiding', models.CharField(default='Naam Opleiding', max_length=35)),
                ('interesse', models.BooleanField(default=False)),
            ],
        ),
    ]
