# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160829_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opleidingen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(default='---', max_length=35)),
                ('naam_opleiding', models.CharField(default='---', max_length=35)),
                ('interesse', models.BooleanField(default=False)),
                ('userprofile', models.ForeignKey(to='main.UserProfile', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='modules',
            name='opleiding',
            field=models.CharField(default='1 november 2016', max_length=35),
        ),
    ]
