# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20160901_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_interesse_opleidingen',
            old_name='user',
            new_name='username',
        ),
    ]
