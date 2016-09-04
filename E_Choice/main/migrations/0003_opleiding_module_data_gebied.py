# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160902_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='opleiding_module_data',
            name='gebied',
            field=models.CharField(default='studie', max_length=50, choices=[('studie', 'studie'), ('sociaal', 'sociaal'), ('toekomst', 'toekomst'), ('studiesociaal', 'studiesociaal'), ('studietoekomst', 'studietoekomst'), ('sociaaltoekomst', 'sociaaltoekomst')]),
        ),
    ]
