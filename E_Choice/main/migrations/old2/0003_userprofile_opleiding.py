# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160902_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile_Opleiding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opleiding', models.CharField(max_length=35, default='Opleiding')),
                ('bank', models.IntegerField(verbose_name='Bank', default=150)),
                ('exp_tot', models.IntegerField(verbose_name='Experience totaal', default=0)),
                ('exp_stud', models.IntegerField(verbose_name='Experience studie', default=0)),
                ('exp_soc', models.IntegerField(verbose_name='Experience sociaal', default=0)),
                ('exp_toek', models.IntegerField(verbose_name='Experience toekomst', default=0)),
                ('niveau', models.IntegerField(verbose_name='Niveau', default=1)),
                ('weging_stud', models.IntegerField(verbose_name='Weging studie', blank=True, default=100)),
                ('weging_soc', models.IntegerField(verbose_name='Weging sociaal', blank=True, default=100)),
                ('weging_toek', models.IntegerField(verbose_name='Weging toekomst', blank=True, default=100)),
                ('userprofile_general', models.ForeignKey(blank=True, to='main.UserProfile_General', null=True)),
            ],
        ),
    ]
