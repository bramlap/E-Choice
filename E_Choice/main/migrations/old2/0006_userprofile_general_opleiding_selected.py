# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_opleiding_module_data_user_interesse_opleidingen'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile_general',
            name='opleiding_selected',
            field=models.CharField(max_length=35, default='None'),
        ),
    ]
