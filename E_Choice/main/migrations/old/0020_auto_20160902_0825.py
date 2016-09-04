# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20160902_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile_general',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile_general',
            name='username',
            field=models.CharField(default='Username', max_length=35),
        ),
    ]
