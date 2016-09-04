# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_opleiding_module_data_gebied'),
    ]

    operations = [
        migrations.AddField(
            model_name='opleiding_module_data',
            name='baten_vast',
            field=models.IntegerField(verbose_name='Vaste baten', default=0),
        ),
    ]
