# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20160831_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile_general',
            name='number_of_logins',
            field=models.IntegerField(verbose_name='# of logins', default=0),
        ),
    ]
