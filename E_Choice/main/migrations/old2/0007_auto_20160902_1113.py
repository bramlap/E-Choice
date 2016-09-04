# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userprofile_general_opleiding_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='opleiding_module_data',
            name='exp_required',
            field=models.IntegerField(verbose_name='Experience benodigd', default=0),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='experience_vast',
            field=models.IntegerField(verbose_name='Vaste exp', default=0),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='factor',
            field=models.PositiveIntegerField(verbose_name='Factor module', default=0),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='id_module',
            field=models.CharField(max_length=15, default=''),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='kosten',
            field=models.IntegerField(verbose_name='Kosten', default=0),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='module_type',
            field=models.CharField(max_length=15, default='Passief', choices=[('Actief', 'Actief'), ('Passief', 'Passief')]),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='naam',
            field=models.CharField(max_length=50, default='NAAM'),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='niveau',
            field=models.IntegerField(verbose_name='Niveau van course', default=1),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='omschrijving',
            field=models.TextField(default='OMSCHRIJVING'),
        ),
        migrations.AddField(
            model_name='opleiding_module_data',
            name='tijd',
            field=models.IntegerField(verbose_name='Tijdsduur', default=0),
        ),
        migrations.AlterField(
            model_name='modules',
            name='date',
            field=models.CharField(max_length=35, default='NONE', choices=[('1 november 2016', '1 november 2016'), ('1 februari 2016', '1 februari 2016'), ('1 april 2016', '1 april 2016')]),
        ),
        migrations.AlterField(
            model_name='modules',
            name='module_type',
            field=models.CharField(max_length=15, default='Passief'),
        ),
        migrations.AlterField(
            model_name='modules',
            name='opleiding',
            field=models.ForeignKey(blank=True, to='main.UserProfile_Opleiding', null=True),
        ),
    ]
