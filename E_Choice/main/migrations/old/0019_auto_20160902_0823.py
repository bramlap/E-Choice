# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20160902_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_general',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
