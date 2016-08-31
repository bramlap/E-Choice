from main.models import Modules, UserProfile
from django.db import models

def run():
    users = UserProfile.objects.all()

    DATES_case = (
                ('date1', '1 dec 2016'),
                ('date2', '1 maart 2016'),
                ('date3', '1 mei 2016'),
    )

    for i in users:
        if i.is_student == True:
            p = Modules(
                gebied='studie',
                naam_gebruiker=str(i)+': Webklas',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                # baten_flex=,
                experience_vast=192,
                # experience_flex=,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                userprofile = i
            )
            p.save()

            p = Modules(
                gebied='toekomst',
                naam_gebruiker=str(i)+': Case',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                # baten_flex=,
                experience_vast= 72,
                # experience_flex=,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                userprofile = i
            )
            p.save()

            p = Modules(
                gebied='sociaal',
                naam_gebruiker = str(i)+': Borrel studievereniging',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                # baten_vast=,
                # baten_flex=,
                experience_vast=48,
                # experience_flex=,
                # factor=,
                niveau=1,
                userprofile = i
            )
            p.save()

            p = Modules(
                gebied='studiesociaal',
                naam_gebruiker = str(i) + ': Een dag student',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                # baten_vast=240,
                # baten_flex=,
                experience_vast=92,
                # experience_flex=,
                # factor=,
                niveau=1,
                userprofile = i,
            )
            p.save()

            p = Modules(
                gebied='studie',
                naam_gebruiker = str(i) + ': Opendag op locatie',
                naam='Opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                # baten_vast=,
                # baten_flex=,
                experience_vast=192,
                # experience_flex=,
                # factor=,
                niveau=1,
                userprofile = i,
            )
            p.save()

            p = Modules(
                gebied='sociaaltoekomst',
                naam_gebruiker = str(i) + ': Excursie met studievereniging',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                # baten_vast=,
                # baten_flex=,
                experience_vast=94,
                # experience_flex=,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                userprofile = i
            )
            p.save()