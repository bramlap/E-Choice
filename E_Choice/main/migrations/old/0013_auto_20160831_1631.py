# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20160831_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Interesse_Opleidingen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('naam_opleiding', models.CharField(default='Naam Opleiding', max_length=35)),
                ('interesse', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Opleidng_module_data',
            new_name='Opleiding_module_data',
        ),
        migrations.RemoveField(
            model_name='opleidingen',
            name='user',
        ),
        migrations.DeleteModel(
            name='Opleidingen',
        ),
    ]
