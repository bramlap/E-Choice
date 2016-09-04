# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_userprofile_general_number_of_logins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_interesse_opleidingen',
            name='user',
            field=models.CharField(default='User', max_length=35),
        ),
    ]
