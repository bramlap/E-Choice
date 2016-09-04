# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile_General',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=1, default='M', choices=[('M', 'Man'), ('V', 'Vrouw')])),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('number_of_logins', models.IntegerField(verbose_name='# of logins', default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='modules',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Modules',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
