# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_modules_date3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='date1',
            field=models.CharField(default='date1', max_length=35),
        ),
        migrations.AlterField(
            model_name='modules',
            name='date2',
            field=models.CharField(default='date2', max_length=35),
        ),
        migrations.AlterField(
            model_name='modules',
            name='date3',
            field=models.CharField(default='date3', max_length=35),
        ),
    ]
