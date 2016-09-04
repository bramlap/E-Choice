from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.utils.functional import lazy
import time, datetime

'''
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
'''

class UserProfile_General(models.Model):
        user = models.OneToOneField(User)

        GENDERS = (
                ('M', 'Man'),
                ('V', 'Vrouw'),
        )
        # General info
        firstname = models.CharField(max_length=50)
        lastname = models.CharField(max_length=50)
        sexe = models.CharField(max_length=1, choices=GENDERS, default='M')
        is_student = models.BooleanField(default=True)
        is_teacher = models.BooleanField(default=False)
        number_of_logins = models.IntegerField('# of logins', default=0)
        opleiding_selected = models.CharField(max_length=35, default='None', blank=True)

        def __str__(self):
                return str(self.user)

class UserProfile_Opleiding(models.Model):
        userprofile_general = models.ForeignKey(UserProfile_General, on_delete=models.CASCADE, blank=True, null=True)

        opleiding = models.CharField(max_length=35, default='Opleiding')
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

        def __str__(self):
                return str(self.userprofile_general)+'_'+self.opleiding

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

        username = models.CharField(max_length=35, default='Username')
        userprofile_opleiding =  models.ForeignKey(UserProfile_Opleiding, on_delete=models.CASCADE, blank=True, null=True)

        opleiding = models.CharField(max_length=35, default='Opleiding')

        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        naam = models.CharField(max_length=50, default="NAAM")

        omschrijving = models.TextField(default="OMSCHRIJVING")
        tijd =  models.IntegerField('Tijdsduur', default=0)
        kosten = models.IntegerField('Kosten', default=0)
        baten_vast = models.IntegerField('Vaste baten', default=0)
        baten_flex = models.IntegerField('Flexibele baten', default=0)
        experience_vast = models.IntegerField('Vaste exp', default=0)
        experience_flex = models.IntegerField('Flexibele exp', default=0)
        factor = models.PositiveIntegerField('Factor module', default=0)
        niveau = models.IntegerField('Niveau van course', default=1)
        module_type = models.CharField(max_length=15, default='Passief')
        cijfer = models.PositiveIntegerField('Cijfer', default=0 , validators=[MaxValueValidator(10),])
        status = models.CharField(max_length=15, choices=STATUS_MODULES, default='Niet gedaan' )
        id_module = models.CharField(max_length=15, default='' )
        buy_module = models.PositiveIntegerField('Module kopen', default=0, blank=True)
        exp_required = models.IntegerField('Experience benodigd', default=0)
        date = models.CharField(max_length=35, choices=DATES, default='NONE')

        #dates
        # date1 = models.DateTimeField(default=datetime.datetime(2016,7,1))
        # date2 = models.DateTimeField(default=datetime.datetime(2016,2,1))
        # date3 = models.DateTimeField(default=datetime.datetime(2016,2,1))
        date1 = models.CharField(max_length=35, default='date1')
        date2 = models.CharField(max_length=35, default='date2')
        date3 = models.CharField(max_length=35, default='date3')

        def __str__(self):
                return self.username+'_'+str(self.opleiding)+'_'+self.naam

class User_Interesse_Opleidingen(models.Model):
        username = models.CharField(max_length=35, default='User')
        naam_opleiding = models.CharField(max_length=35, default='Naam Opleiding')
        interesse = models.BooleanField(default=False)

        def __str__(self):
                return str(self.username)+'_'+self.naam_opleiding

class Opleiding_module_data(models.Model):
        TYPES_MODULES = (
                ('Actief', 'Actief'),
                ('Passief', 'Passief')
        )
        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        opleiding = models.CharField(max_length=35, default='Opleiding')
        module = models.CharField(max_length=35, default='module')
        naam = models.CharField(max_length=50, default="NAAM")
        id_module = models.CharField(max_length=15, default='' )
        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        omschrijving = omschrijving = models.TextField(default="OMSCHRIJVING")
        module_type = models.CharField(max_length=15, choices=TYPES_MODULES, default='Passief')

        tijd =  models.IntegerField('Tijdsduur', default=0)
        kosten = models.IntegerField('Kosten', default=0)
        baten_vast = models.IntegerField('Vaste baten', default=0)
        experience_vast = models.IntegerField('Vaste exp', default=0)
        exp_required = models.IntegerField('Experience benodigd', default=0)
        niveau = models.IntegerField('Niveau van course', default=1)
        factor = models.PositiveIntegerField('Factor module', default=0)

        date1 = models.CharField(max_length=35, default='date1')
        date2 = models.CharField(max_length=35, default='date2')
        date3 = models.CharField(max_length=35, default='date3')

        def __str__(self):
                return self.opleiding+'_'+self.module

'''

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

class User_Interesse_Opleidingen(models.Model):
        username = models.CharField(max_length=35, default='User')
        naam_opleiding = models.CharField(max_length=35, default='Naam Opleiding')
        interesse = models.BooleanField(default=False)
        # naam_module = models.CharField(max_length=50, default="NAAM")

        # date1 = models.CharField(max_length=50, default="DATE1")
        # date2 = models.CharField(max_length=50, default="DATE2")
        # date3 = models.CharField(max_length=50, default="DATE3")

        # wiskunde = models.BooleanField(default=False)
        # natuurkunde = models.BooleanField(default=False)
        # sterrenkunde = models.BooleanField(default=False)
        # scheikunde = models.BooleanField(default=False)
        # biologie = models.BooleanField(default=False)
        # lst = models.BooleanField(default=False)
        # farmacie = models.BooleanField(default=False)
        # informatica = models.BooleanField(default=False)
        # ki = models.BooleanField(default=False)
        # tbk = models.BooleanField(default=False)

        def __str__(self):
                return str(self.username)+'_'+self.naam_opleiding

class Opleiding_module_data(models.Model):
        opleiding = models.CharField(max_length=35, default='Opleiding')
        module = models.CharField(max_length=35, default='module')
        date1 = models.CharField(max_length=35, default='date1')
        date2 = models.CharField(max_length=35, default='date2')
        date3 = models.CharField(max_length=35, default='date3')

        def __str__(self):
                return self.opleiding+'_'+self.module
'''