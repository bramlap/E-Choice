# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_opleidng_module_data_userprofile_general_userprofile_opleiding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opleidingen',
            name='username',
        ),
        migrations.RemoveField(
            model_name='opleidingen',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='opleidingen',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
