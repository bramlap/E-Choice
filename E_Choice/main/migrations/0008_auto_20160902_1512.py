# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160902_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_general',
            name='opleiding_selected',
            field=models.CharField(default='None', blank=True, max_length=35),
        ),
    ]
