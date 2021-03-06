# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 11:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gebied', models.CharField(choices=[('studie', 'studie'), ('sociaal', 'sociaal'), ('toekomst', 'toekomst'), ('studiesociaal', 'studiesociaal'), ('studietoekomst', 'studietoekomst'), ('sociaaltoekomst', 'sociaaltoekomst')], default='studie', max_length=50)),
                ('naam', models.CharField(default='NAAM', max_length=50)),
                ('naam_gebruiker', models.CharField(default='NAAM_GEBRUIKER', max_length=50)),
                ('omschrijving', models.TextField(default='OMSCHRIJVING')),
                ('tijd', models.IntegerField(default=0, verbose_name='Tijdsduur')),
                ('kosten', models.IntegerField(default=0, verbose_name='Kosten')),
                ('baten_vast', models.IntegerField(default=0, verbose_name='Vaste baten')),
                ('baten_flex', models.IntegerField(default=0, verbose_name='Flexibele baten')),
                ('experience_vast', models.IntegerField(default=0, verbose_name='Vaste exp')),
                ('experience_flex', models.IntegerField(default=0, verbose_name='Flexibele exp')),
                ('factor', models.PositiveIntegerField(default=0, verbose_name='Factor module')),
                ('niveau', models.IntegerField(default=1, verbose_name='Niveau van course')),
                ('module_type', models.CharField(choices=[('Actief', 'Actief'), ('Passief', 'Passief')], default='Passief', max_length=15)),
                ('cijfer', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)], verbose_name='Cijfer')),
                ('status', models.CharField(choices=[('Niet gedaan', 'Niet gedaan'), ('Bezig', 'Bezig'), ('Voltooid', 'Voltooid')], default='Niet gedaan', max_length=15)),
                ('id_module', models.CharField(default='', max_length=15)),
                ('buy_module', models.PositiveIntegerField(default=0, verbose_name='Module kopen')),
                ('exp_required', models.IntegerField(default=0, verbose_name='Experience benodigd')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam_question_gebruiker', models.CharField(default='NAAM_QUESTION_GEBRUIKER', max_length=50)),
                ('question', models.TextField(default='QUESTION')),
                ('answers', models.CharField(choices=[('Ja', 'Ja'), ('Nee', 'Nee'), ('WN', 'Weet niet')], default='WN', max_length=50)),
                ('gebied', models.CharField(choices=[('studie', 'studie'), ('sociaal', 'sociaal'), ('toekomst', 'toekomst'), ('studiesociaal', 'studiesociaal'), ('studietoekomst', 'studietoekomst'), ('sociaaltoekomst', 'sociaaltoekomst')], default='studie', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('sexe', models.CharField(choices=[('M', 'Man'), ('V', 'Vrouw')], default='M', max_length=1)),
                ('bank', models.IntegerField(default=150, verbose_name='Bank')),
                ('exp_tot', models.IntegerField(default=0, verbose_name='Experience totaal')),
                ('exp_stud', models.IntegerField(default=0, verbose_name='Experience studie')),
                ('exp_soc', models.IntegerField(default=0, verbose_name='Experience sociaal')),
                ('exp_toek', models.IntegerField(default=0, verbose_name='Experience toekomst')),
                ('niveau', models.IntegerField(default=1, verbose_name='Niveau')),
                ('weging_stud', models.IntegerField(blank=True, default=100, verbose_name='Weging studie')),
                ('weging_soc', models.IntegerField(blank=True, default=100, verbose_name='Weging sociaal')),
                ('weging_toek', models.IntegerField(blank=True, default=100, verbose_name='Weging toekomst')),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
        migrations.AddField(
            model_name='modules',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
    ]
