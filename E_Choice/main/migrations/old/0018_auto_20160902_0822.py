# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_auto_20160901_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile_general',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile_general',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
