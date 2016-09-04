# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opleiding_module_data',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('opleiding', models.CharField(max_length=35, default='Opleiding')),
                ('module', models.CharField(max_length=35, default='module')),
                ('naam', models.CharField(max_length=50, default='NAAM')),
                ('id_module', models.CharField(max_length=15, default='')),
                ('omschrijving', models.TextField(default='OMSCHRIJVING')),
                ('module_type', models.CharField(max_length=15, choices=[('Actief', 'Actief'), ('Passief', 'Passief')], default='Passief')),
                ('tijd', models.IntegerField(verbose_name='Tijdsduur', default=0)),
                ('kosten', models.IntegerField(verbose_name='Kosten', default=0)),
                ('experience_vast', models.IntegerField(verbose_name='Vaste exp', default=0)),
                ('exp_required', models.IntegerField(verbose_name='Experience benodigd', default=0)),
                ('niveau', models.IntegerField(verbose_name='Niveau van course', default=1)),
                ('factor', models.PositiveIntegerField(verbose_name='Factor module', default=0)),
                ('date1', models.CharField(max_length=35, default='date1')),
                ('date2', models.CharField(max_length=35, default='date2')),
                ('date3', models.CharField(max_length=35, default='date3')),
            ],
        ),
        migrations.CreateModel(
            name='User_Interesse_Opleidingen',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=35, default='User')),
                ('naam_opleiding', models.CharField(max_length=35, default='Naam Opleiding')),
                ('interesse', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile_General',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=1, choices=[('M', 'Man'), ('V', 'Vrouw')], default='M')),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('number_of_logins', models.IntegerField(verbose_name='# of logins', default=0)),
                ('opleiding_selected', models.CharField(max_length=35, default='None')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile_Opleiding',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('userprofile_general', models.ForeignKey(null=True, blank=True, to='main.UserProfile_General')),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='naam_gebruiker',
        ),
        migrations.RemoveField(
            model_name='modules',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='modules',
            name='date',
            field=models.CharField(max_length=35, choices=[('1 november 2016', '1 november 2016'), ('1 februari 2016', '1 februari 2016'), ('1 april 2016', '1 april 2016')], default='NONE'),
        ),
        migrations.AddField(
            model_name='modules',
            name='date1',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='modules',
            name='date2',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 1, 0, 0)),
        ),
        migrations.AddField(
            model_name='modules',
            name='username',
            field=models.CharField(max_length=35, default='Username'),
        ),
        migrations.AlterField(
            model_name='modules',
            name='buy_module',
            field=models.PositiveIntegerField(verbose_name='Module kopen', blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='modules',
            name='module_type',
            field=models.CharField(max_length=15, default='Passief'),
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='modules',
            name='opleiding',
            field=models.ForeignKey(null=True, blank=True, to='main.UserProfile_Opleiding'),
        ),
    ]
