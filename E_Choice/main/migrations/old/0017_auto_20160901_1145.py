# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160901_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile_general',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile_opleiding',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile_general',
            name='username',
            field=models.CharField(default='Username', max_length=35),
        ),
        migrations.AddField(
            model_name='userprofile_opleiding',
            name='username',
            field=models.CharField(default='Username', max_length=35),
        ),
    ]
