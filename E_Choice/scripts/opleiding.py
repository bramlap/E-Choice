from main.models import Modules, UserProfile, Opleidingen
from django.db import models

def run():
    users = UserProfile.objects.all()

    opleidingen = [ 'wiskunde',
                    'natuurkunde',
                    'sterrenkunde',
                    'scheikunde',
                    'biologie',
                    'lst',
                    'farmacie',
                    'informatica',
                    'ki',
                    'tbk',
    ]

    id_module = [   'webklas',
                    'case',
                    'borrel',
                    'dag_student',
                    'opendag',
                    'excursie',
    ]

    for i in users:
        for j in opleidingen:
            if i.is_student == True:
                p = Opleidingen(
                    userprofile = i,
                    username = str(i),
                    naam_opleiding = str(j),
                )
                print(p)
                p.save()