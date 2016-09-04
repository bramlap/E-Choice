# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_userprofile_opleiding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(default='Username', max_length=35)),
                ('gebied', models.CharField(choices=[('studie', 'studie'), ('sociaal', 'sociaal'), ('toekomst', 'toekomst'), ('studiesociaal', 'studiesociaal'), ('studietoekomst', 'studietoekomst'), ('sociaaltoekomst', 'sociaaltoekomst')], default='studie', max_length=50)),
                ('naam', models.CharField(default='NAAM', max_length=50)),
                ('omschrijving', models.TextField(default='OMSCHRIJVING')),
                ('tijd', models.IntegerField(verbose_name='Tijdsduur', default=0)),
                ('kosten', models.IntegerField(verbose_name='Kosten', default=0)),
                ('baten_vast', models.IntegerField(verbose_name='Vaste baten', default=0)),
                ('baten_flex', models.IntegerField(verbose_name='Flexibele baten', default=0)),
                ('experience_vast', models.IntegerField(verbose_name='Vaste exp', default=0)),
                ('experience_flex', models.IntegerField(verbose_name='Flexibele exp', default=0)),
                ('factor', models.PositiveIntegerField(verbose_name='Factor module', default=0)),
                ('niveau', models.IntegerField(verbose_name='Niveau van course', default=1)),
                ('module_type', models.CharField(choices=[('Actief', 'Actief'), ('Passief', 'Passief')], default='Passief', max_length=15)),
                ('cijfer', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Cijfer', default=0)),
                ('status', models.CharField(choices=[('Niet gedaan', 'Niet gedaan'), ('Bezig', 'Bezig'), ('Voltooid', 'Voltooid')], default='Niet gedaan', max_length=15)),
                ('id_module', models.CharField(default='', max_length=15)),
                ('buy_module', models.PositiveIntegerField(blank=True, default=0, verbose_name='Module kopen')),
                ('exp_required', models.IntegerField(verbose_name='Experience benodigd', default=0)),
                ('date', models.CharField(choices=[('1 november 2016', '1 november 2016'), ('1 februari 2016', '1 februari 2016'), ('1 april 2016', '1 april 2016')], default='1 november 2016', max_length=35)),
                ('opleiding', models.CharField(default='1 november 2016', max_length=35)),
                ('date1', models.DateTimeField(default=datetime.datetime(2016, 7, 1, 0, 0))),
                ('date2', models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0))),
            ],
        ),
    ]
