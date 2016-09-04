# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20160831_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opleidng_module_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('opleiding', models.CharField(default='Opleiding', max_length=35)),
                ('module', models.CharField(default='module', max_length=35)),
                ('date1', models.CharField(default='date1', max_length=35)),
                ('date2', models.CharField(default='date2', max_length=35)),
                ('date3', models.CharField(default='date3', max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile_General',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('sexe', models.CharField(default='M', choices=[('M', 'Man'), ('V', 'Vrouw')], max_length=1)),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile_Opleiding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('opleiding', models.CharField(default='Opleiding', max_length=35)),
                ('bank', models.IntegerField(default=150, verbose_name='Bank')),
                ('exp_tot', models.IntegerField(default=0, verbose_name='Experience totaal')),
                ('exp_stud', models.IntegerField(default=0, verbose_name='Experience studie')),
                ('exp_soc', models.IntegerField(default=0, verbose_name='Experience sociaal')),
                ('exp_toek', models.IntegerField(default=0, verbose_name='Experience toekomst')),
                ('niveau', models.IntegerField(default=1, verbose_name='Niveau')),
                ('weging_stud', models.IntegerField(default=100, verbose_name='Weging studie', blank=True)),
                ('weging_soc', models.IntegerField(default=100, verbose_name='Weging sociaal', blank=True)),
                ('weging_toek', models.IntegerField(default=100, verbose_name='Weging toekomst', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
