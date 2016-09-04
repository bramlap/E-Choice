from main.models import Opleiding_module_data

def run():
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

    id_modules = [ 'opendag',
            'webklas',
            'dag_student'
            'case',
            'excursie',
            'borrel'
    ]

        # opleiding = models.CharField(max_length=35, default='Opleiding')
        # module = models.CharField(max_length=35, default='module')
        # naam = models.CharField(max_length=50, default="NAAM")
        # id_module = models.CharField(max_length=15, default='' )
        # omschrijving = omschrijving = models.TextField(default="OMSCHRIJVING")
        # module_type = models.CharField(max_length=15, choices=TYPES_MODULES, default='Passief')

        # tijd =  models.IntegerField('Tijdsduur', default=0)
        # kosten = models.IntegerField('Kosten', default=0)
        # experience_vast = models.IntegerField('Vaste exp', default=0)
        # exp_required = models.IntegerField('Experience benodigd', default=0)
        # niveau = models.IntegerField('Niveau van course', default=1)
        # factor = models.PositiveIntegerField('Factor module', default=0)

        # date1 = models.CharField(max_length=35, default='date1')
        # date2 = models.CharField(max_length=35, default='date2')
        # date3 = models.CharField(max_length=35, default='date3')
            
        # #Webklas
        #         gebied='studie',
        #         naam = 'Webklas',
        #         id_module = 'webklas',
        #         omschrijving='Online cursus over bepaalde bachelor opleidingen',
        #         tijd=16,
        #         kosten=240,
        #         baten_vast=240,
        #         experience_vast=192,
        #         factor=50,
        #         module_type = 'Actief',
        #         niveau=2,

        #         gebied='studiesociaal',
        #         naam='Een dag student',
        #         id_module = 'dag_student',
        #         omschrijving='Een dagje student zijn',
        #         tijd=8,
        #         kosten=120,
        #         baten_vast=240,
        #         experience_vast=92,
        #         niveau=1,

        #         gebied='toekomst',
        #         naam = 'Case voor een bedrijf',
        #         id_module = 'case',
        #         omschrijving='Een probleem oplossen voor een bedrijf',
        #         tijd=3,
        #         kosten=45,
        #         baten_vast=45,
        #         experience_vast= 72,
        #         factor=30,
        #         module_type = 'Actief',
        #         niveau=1,

        #         gebied='sociaal',
        #         naam='Borrel studievereniging',
        #         id_module = 'borrel',
        #         omschrijving='Vrijdag middag borrel met lezing/praatje',
        #         tijd=2,
        #         kosten=60,
        #         experience_vast=48,
        #         niveau=1,

        #         gebied='studie',
        #         naam_gebruiker = str(i) + ': opendag op locatie',
        #         naam='opendag op locatie',
        #         id_module = 'opendag',
        #         omschrijving='Een specifieke opleiding beter leren kennen',
        #         tijd=8,
        #         kosten=240,
        #         experience_vast=192,
        #         niveau=1,

        #         gebied='sociaaltoekomst',
        #         naam='Excursie met studievereniging',
        #         id_module = 'excursie',
        #         omschrijving='Bij een bedrijf op bezoek',
        #         tijd=4,
        #         kosten=120,
        #         experience_vast=94,
        #         factor=30,
        #         module_type = 'Actief',
        #         niveau=2,


    #wiskunde
    wiskunde_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    wiskunde_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    wiskunde_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    wiskunde_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    wiskunde_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    wiskunde_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #Natuurkunde 
    natuurkunde_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    natuurkunde_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    natuurkunde_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    natuurkunde_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    natuurkunde_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    natuurkunde_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #scheikunde
    scheikunde_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    scheikunde_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    scheikunde_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    scheikunde_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    scheikunde_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    scheikunde_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #sterrenkunde
    sterrenkunde_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    sterrenkunde_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    sterrenkunde_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    sterrenkunde_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    sterrenkunde_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    sterrenkunde_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #biologie
    biologie_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    biologie_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    biologie_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    biologie_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    biologie_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    biologie_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #lst
    lst_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    lst_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    lst_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    lst_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    lst_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    lst_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #farmacie
    farmacie_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    farmacie_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    farmacie_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    farmacie_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    farmacie_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    farmacie_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #informatica
    informatica_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    informatica_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    informatica_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    informatica_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    informatica_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    informatica_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #ki
    ki_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    ki_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    ki_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    ki_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    ki_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    ki_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    #tbk
    tbk_opendag = [ '1/11/2016', '1/2/2017', '1/4/2017']
    tbk_webklas = [ '1/11/2016', '1/2/2017', '1/4/2017']
    tbk_dag_student = [ '1/11/2016', '1/2/2017', '1/4/2017']
    tbk_case = [ '1/11/2016', '1/2/2017', '1/4/2017']
    tbk_excursie = [ '1/11/2016', '1/2/2017', '1/4/2017']
    tbk_borrel = [ '1/11/2016', '1/2/2017', '1/4/2017']

    for i in opleidingen:
        if i == 'wiskunde':
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(wiskunde_opendag[0]),
                date2 = str(wiskunde_opendag[1]),
                date3 = str(wiskunde_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(wiskunde_webklas[0]),
                date2 = str(wiskunde_webklas[1]),
                date3 = str(wiskunde_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(wiskunde_dag_student[0]),
                date2 = str(wiskunde_dag_student[1]),
                date3 = str(wiskunde_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(wiskunde_case[0]),
                date2 = str(wiskunde_case[1]),
                date3 = str(wiskunde_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(wiskunde_excursie[0]),
                date2 = str(wiskunde_excursie[1]),
                date3 = str(wiskunde_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'wiskunde',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(wiskunde_borrel[0]),
                date2 = str(wiskunde_borrel[1]),
                date3 = str(wiskunde_borrel[2]),
                )
            p.save()
        if i == 'natuurkunde':
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                module = 'opendag',
                date1 = str(natuurkunde_opendag[0]),
                date2 = str(natuurkunde_opendag[1]),
                date3 = str(natuurkunde_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(natuurkunde_webklas[0]),
                date2 = str(natuurkunde_webklas[1]),
                date3 = str(natuurkunde_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(natuurkunde_dag_student[0]),
                date2 = str(natuurkunde_dag_student[1]),
                date3 = str(natuurkunde_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(natuurkunde_case[0]),
                date2 = str(natuurkunde_case[1]),
                date3 = str(natuurkunde_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(natuurkunde_excursie[0]),
                date2 = str(natuurkunde_excursie[1]),
                date3 = str(natuurkunde_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'natuurkunde',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(natuurkunde_borrel[0]),
                date2 = str(natuurkunde_borrel[1]),
                date3 = str(natuurkunde_borrel[2]),
                )
            p.save()
        if i == 'scheikunde':
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                module = 'opendag',
                date1 = str(scheikunde_opendag[0]),
                date2 = str(scheikunde_opendag[1]),
                date3 = str(scheikunde_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(scheikunde_webklas[0]),
                date2 = str(scheikunde_webklas[1]),
                date3 = str(scheikunde_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(scheikunde_dag_student[0]),
                date2 = str(scheikunde_dag_student[1]),
                date3 = str(scheikunde_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(scheikunde_case[0]),
                date2 = str(scheikunde_case[1]),
                date3 = str(scheikunde_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(scheikunde_excursie[0]),
                date2 = str(scheikunde_excursie[1]),
                date3 = str(scheikunde_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'scheikunde',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(scheikunde_borrel[0]),
                date2 = str(scheikunde_borrel[1]),
                date3 = str(scheikunde_borrel[2]),
                )
            p.save()
        if i == 'sterrenkunde':
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(sterrenkunde_opendag[0]),
                date2 = str(sterrenkunde_opendag[1]),
                date3 = str(sterrenkunde_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(sterrenkunde_webklas[0]),
                date2 = str(sterrenkunde_webklas[1]),
                date3 = str(sterrenkunde_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(sterrenkunde_dag_student[0]),
                date2 = str(sterrenkunde_dag_student[1]),
                date3 = str(sterrenkunde_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(sterrenkunde_case[0]),
                date2 = str(sterrenkunde_case[1]),
                date3 = str(sterrenkunde_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(sterrenkunde_excursie[0]),
                date2 = str(sterrenkunde_excursie[1]),
                date3 = str(sterrenkunde_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'sterrenkunde',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(sterrenkunde_borrel[0]),
                date2 = str(sterrenkunde_borrel[1]),
                date3 = str(sterrenkunde_borrel[2]),
                )
            p.save()
        if i == 'biologie':
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(biologie_opendag[0]),
                date2 = str(biologie_opendag[1]),
                date3 = str(biologie_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(biologie_webklas[0]),
                date2 = str(biologie_webklas[1]),
                date3 = str(biologie_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(biologie_dag_student[0]),
                date2 = str(biologie_dag_student[1]),
                date3 = str(biologie_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(biologie_case[0]),
                date2 = str(biologie_case[1]),
                date3 = str(biologie_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(biologie_excursie[0]),
                date2 = str(biologie_excursie[1]),
                date3 = str(biologie_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'biologie',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(biologie_borrel[0]),
                date2 = str(biologie_borrel[1]),
                date3 = str(biologie_borrel[2]),
                )
            p.save()
        if i == 'lst':
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(lst_opendag[0]),
                date2 = str(lst_opendag[1]),
                date3 = str(lst_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(lst_webklas[0]),
                date2 = str(lst_webklas[1]),
                date3 = str(lst_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(lst_dag_student[0]),
                date2 = str(lst_dag_student[1]),
                date3 = str(lst_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(lst_case[0]),
                date2 = str(lst_case[1]),
                date3 = str(lst_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(lst_excursie[0]),
                date2 = str(lst_excursie[1]),
                date3 = str(lst_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'lst',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(lst_borrel[0]),
                date2 = str(lst_borrel[1]),
                date3 = str(lst_borrel[2]),
                )
            p.save()
        if i == 'farmacie':
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(farmacie_opendag[0]),
                date2 = str(farmacie_opendag[1]),
                date3 = str(farmacie_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(farmacie_webklas[0]),
                date2 = str(farmacie_webklas[1]),
                date3 = str(farmacie_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(farmacie_dag_student[0]),
                date2 = str(farmacie_dag_student[1]),
                date3 = str(farmacie_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(farmacie_case[0]),
                date2 = str(farmacie_case[1]),
                date3 = str(farmacie_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(farmacie_excursie[0]),
                date2 = str(farmacie_excursie[1]),
                date3 = str(farmacie_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'farmacie',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(farmacie_borrel[0]),
                date2 = str(farmacie_borrel[1]),
                date3 = str(farmacie_borrel[2]),
                )
            p.save()
        if i == 'informatica':
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(informatica_opendag[0]),
                date2 = str(informatica_opendag[1]),
                date3 = str(informatica_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(informatica_webklas[0]),
                date2 = str(informatica_webklas[1]),
                date3 = str(informatica_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(informatica_dag_student[0]),
                date2 = str(informatica_dag_student[1]),
                date3 = str(informatica_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(informatica_case[0]),
                date2 = str(informatica_case[1]),
                date3 = str(informatica_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(informatica_excursie[0]),
                date2 = str(informatica_excursie[1]),
                date3 = str(informatica_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'informatica',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(informatica_borrel[0]),
                date2 = str(informatica_borrel[1]),
                date3 = str(informatica_borrel[2]),
                )
            p.save()
        if i == 'ki':
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(ki_opendag[0]),
                date2 = str(ki_opendag[1]),
                date3 = str(ki_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(ki_webklas[0]),
                date2 = str(ki_webklas[1]),
                date3 = str(ki_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(ki_dag_student[0]),
                date2 = str(ki_dag_student[1]),
                date3 = str(ki_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(ki_case[0]),
                date2 = str(ki_case[1]),
                date3 = str(ki_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(ki_excursie[0]),
                date2 = str(ki_excursie[1]),
                date3 = str(ki_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'ki',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(ki_borrel[0]),
                date2 = str(ki_borrel[1]),
                date3 = str(ki_borrel[2]),
                )
            p.save()
        if i == 'tbk':
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'opendag',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = str(tbk_opendag[0]),
                date2 = str(tbk_opendag[1]),
                date3 = str(tbk_opendag[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'webklas',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = str(tbk_webklas[0]),
                date2 = str(tbk_webklas[1]),
                date3 = str(tbk_webklas[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'dag_student',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = str(tbk_dag_student[0]),
                date2 = str(tbk_dag_student[1]),
                date3 = str(tbk_dag_student[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'case',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = str(tbk_case[0]),
                date2 = str(tbk_case[1]),
                date3 = str(tbk_case[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'excursie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = str(tbk_excursie[0]),
                date2 = str(tbk_excursie[1]),
                date3 = str(tbk_excursie[2]),
                )
            p.save()
            p = Opleiding_module_data(
                opleiding = 'tbk',
                module = 'borrel',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = str(tbk_borrel[0]),
                date2 = str(tbk_borrel[1]),
                date3 = str(tbk_borrel[2]),
                )
            p.save()