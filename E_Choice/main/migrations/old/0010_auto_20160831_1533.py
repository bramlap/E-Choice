# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160830_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opleidingen',
            name='naam_opleiding',
            field=models.CharField(default='Naam Opleiding', max_length=35),
        ),
        migrations.AlterField(
            model_name='opleidingen',
            name='username',
            field=models.CharField(default='Username', max_length=35),
        ),
    ]
