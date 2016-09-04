# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_opleiding_module_data_baten_vast'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='date3',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0)),
        ),
    ]
