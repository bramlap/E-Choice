from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils.functional import lazy
import time, datetime

class UserProfile(models.Model):
        user = models.OneToOneField(User)

        # additional information
        GENDERS = (
                ('M', 'Man'),
                ('V', 'Vrouw'),
        )
        # General info
        firstname = models.CharField(max_length=50)
        lastname = models.CharField(max_length=50)
        sexe = models.CharField(max_length=1, choices=GENDERS, default='M')
        bank = models.IntegerField('Bank', default=150)
        exp_tot = models.IntegerField('Experience totaal', default=0)
        exp_stud = models.IntegerField('Experience studie', default=0)
        exp_soc = models.IntegerField('Experience sociaal', default=0)
        exp_toek = models.IntegerField('Experience toekomst', default=0)
        niveau = models.IntegerField('Niveau', default=1)

        # Weging voor piechart enzo
        weging_stud = models.IntegerField('Weging studie', default=100, blank=True)
        weging_soc = models.IntegerField('Weging sociaal', default=100, blank=True)
        weging_toek = models.IntegerField('Weging toekomst', default=100, blank=True)

        is_student = models.BooleanField(default=True)
        is_teacher = models.BooleanField(default=False)

        # relations bitches
        # modules = models.ForeignKey(Modules, on_delete=models.CASCADE, blank=True, null=True)
        # questions = models.ForeignKey(Questions, on_delete=models.CASCADE, blank=True, null=True)
        # modules = models.ToManyField(Modules, on_delete=models.CASCADE, blank=True, null=True)

        def __str__(self):
                return self.user.username

class Modules(models.Model):
        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        TYPES_MODULES = (
                ('Actief', 'Actief'),
                ('Passief', 'Passief')
        )

        STATUS_MODULES = (
                ('Niet gedaan', 'Niet gedaan'),
                ('Bezig', 'Bezig'),
                ('Voltooid', 'Voltooid')
        )

        DATES = (
                ('1 november 2016', '1 november 2016'),
                ('1 februari 2016', '1 februari 2016'),
                ('1 april 2016', '1 april 2016')
        )

        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        naam = models.CharField(max_length=50, default="NAAM")
        naam_gebruiker = models.CharField(max_length=50 , default = "NAAM_GEBRUIKER")
        omschrijving = models.TextField(default="OMSCHRIJVING")
        tijd =  models.IntegerField('Tijdsduur', default=0)
        kosten = models.IntegerField('Kosten', default=0)
        baten_vast = models.IntegerField('Vaste baten', default=0)
        baten_flex = models.IntegerField('Flexibele baten', default=0)
        experience_vast = models.IntegerField('Vaste exp', default=0)
        experience_flex = models.IntegerField('Flexibele exp', default=0)
        factor = models.PositiveIntegerField('Factor module', default=0)
        niveau = models.IntegerField('Niveau van course', default=1)
        module_type = models.CharField(max_length=15, choices=TYPES_MODULES, default='Passief')
        cijfer = models.PositiveIntegerField('Cijfer', default=0 , validators=[MaxValueValidator(10),])
        status = models.CharField(max_length=15, choices=STATUS_MODULES, default='Niet gedaan' )
        id_module = models.CharField(max_length=15, default='' )
        buy_module = models.PositiveIntegerField('Module kopen', default=0, blank=True)
        exp_required = models.IntegerField('Experience benodigd', default=0)
        date = models.CharField(max_length=35, choices=DATES, default='1 november 2016')

        #dates
        date1 = models.DateTimeField(default=datetime.datetime(2016,7,1))
        date2 = models.DateTimeField(default=datetime.datetime(2016,2,1))

        userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)

        def __str__(self):
                return self.naam_gebruiker


class Questions(models.Model):
        CHOICES = (
                ('Ja', 'Ja'),
                ('Nee', 'Nee'),
                ('WN', 'Weet niet')
        )

        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        naam_question_gebruiker = models.CharField(max_length=50 , default = "NAAM_QUESTION_GEBRUIKER")
        question = models.TextField(default="QUESTION")
        answers = models.CharField(max_length=50, choices=CHOICES, default='WN')
        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        timestamp = models.DateTimeField(auto_now=True)

        userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)

        def __str__(self):
                return self.naam_question_gebruiker



