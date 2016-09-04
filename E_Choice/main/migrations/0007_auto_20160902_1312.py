# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160902_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='userprofile_opleiding',
            field=models.ForeignKey(null=True, blank=True, to='main.UserProfile_Opleiding'),
        ),
        migrations.AlterField(
            model_name='modules',
            name='opleiding',
            field=models.CharField(default='Opleiding', max_length=35),
        ),
    ]
