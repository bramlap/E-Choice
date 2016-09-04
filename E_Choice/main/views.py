from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .models import  UserProfile_General, Modules, UserProfile_Opleiding, User_Interesse_Opleidingen, Opleiding_module_data
# Modules, Questions, UserProfile,, UserProfile_Opleiding, User_Interesse_Opleidingen
import numpy as np
from .forms import UserOpleidingKiezenForm, BuyModuleForm, SelecteerOpleidingForm, UserProfileOpleidingForm, SelecteerStudentForm, ModuleForm
# UserProfileForm, QuestionForm, ModuleForm, , ExportPDFForm, ModulesDatesForm, 
from reportlab.pdfgen import canvas
from django.template.loader import get_template

from weasyprint import HTML, CSS
from django.template import RequestContext
from django.conf import settings

import time

def login(request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/loggedin')
        else:
            username = request.POST.get('username', "")
            password = request.POST.get('password', "")
            if username != "":
                    user = auth.authenticate(username=username,
                                             password=password)
                    if user is not None:
                        if user.userprofile_general.is_student:
                            auth.login(request, user)
                            return HttpResponseRedirect('/loggedin')
                        if user.userprofile_general.is_teacher:
                            auth.login(request, user)
                            return HttpResponseRedirect('/docent')

                    else:
                            error = 'invalide username or password!'
                            form = 'registration/login.html'
                            return render(request,
                                          form,
                                          {'error_value': error})
            else:
                    form = 'registration/login.html'
                    error = ''
                    return render(request, form, {'error_value': error})

def opleiding_kiezen(request):

    form = 'main/opleiding_kiezen.html'
    Gebruiker = request.user

    form_opleiding_kiezen = UserOpleidingKiezenForm()

    if request.method == "POST":
        data_request = request.POST

        response = {'Gebruiker':Gebruiker, 'form_opleiding_kiezen':form_opleiding_kiezen,
                    'data_request':data_request,
        }

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

        # for i in data_request:
        #     for j in opleidingen:
        #         if i == j:
        #             print(i)
        #             p = User_Interesse_Opleidingen(
        #                 username = str(request.user),
        #                 naam_opleiding = str(j),
        #                 interesse = True
        #             )
        #             p.save()

        userprofile_general = UserProfile_General.objects.get(user=Gebruiker)

        if str(userprofile_general.is_teacher) != 'teacher':
            user_interesse_opleiding = User_Interesse_Opleidingen.objects.filter(username=str(userprofile_general.user))
            if len(user_interesse_opleiding) != 0:
                for k in range(len(user_interesse_opleiding)):
                    if k == 0:
                        temp = userprofile_general
                        temp.opleiding_selected = user_interesse_opleiding[0].naam_opleiding
                        temp.save()

                    p = UserProfile_Opleiding(
                        userprofile_general = userprofile_general,
                        opleiding = str(user_interesse_opleiding[k].naam_opleiding)
                    )
                    p.save()

                    opleiding_module_data = Opleiding_module_data.objects.filter(opleiding=str(user_interesse_opleiding[k].naam_opleiding))
                    for i in opleiding_module_data:
                        a = Modules(
                            username = str(Gebruiker) ,
                            userprofile_opleiding =  p ,
                            opleiding = str(user_interesse_opleiding[k].naam_opleiding),
                            gebied = i.gebied, 
                            naam = i.naam,
                            omschrijving = i.omschrijving,
                            tijd =  i.tijd,
                            kosten = i.kosten,
                            baten_vast = i.baten_vast,
                            experience_vast = i.factor,
                            factor =i.factor,
                            niveau = i.niveau,
                            module_type = i.module_type,
                            id_module = i.id_module,
                            date1 = i.date1,
                            date2 = i.date2,
                            date3 = i.date3,
                        )
                        a.save()

        return render(request, form, response )

    else:
        response = {'Gebruiker':Gebruiker, 'form_opleiding_kiezen':form_opleiding_kiezen,
        }

        return render(request, form, response )

def loggedin(request):

        Gebruiker = request.user.userprofile_general
        if Gebruiker.is_student == True :

            need_save = 0
            if not request.user.is_authenticated():
                    return HttpResponseRedirect('/login')
            else:

                Gebruiker = request.user.userprofile_general
                firstname = Gebruiker.firstname
                lastname = Gebruiker.lastname                            

                form_buy_module_list = []
                form_dates_module_list = []
                data_user_general = UserProfile_General.objects.all().get(firstname=firstname, lastname=lastname)

                data_user_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker)
                user_selected_opleiding = Gebruiker.opleiding_selected
                
                # Selecteer opleiding
                data_request = 0
                if request.method == "POST":
                    if request.POST.get('opleiding_selected'):
                        Gebruiker.opleiding_selected = request.POST['opleiding_selected']
                        Gebruiker.save();

                user_selected_opleiding = Gebruiker.opleiding_selected

                data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker, opleiding=str(user_selected_opleiding))
                user = data_user_selected_opleiding[0]
                data_user_selected_opleiding_modules = Modules.objects.filter(username=str(Gebruiker), userprofile_opleiding=data_user_selected_opleiding)

                user_opleiding_modules = data_user_selected_opleiding_modules
                modules = data_user_selected_opleiding_modules

                form_buy_module_list = []

                # #Buying a module!
                data_request = 0
                to_save = 0
                if request.method == "POST":
                    data_request = request.POST
                    for i in data_request:
                        for p in range(len(user_opleiding_modules)):
                            if i == str(user_opleiding_modules[p].id_module)+'-buy_module':
                                to_save = user_opleiding_modules[p]
                                print(to_save)
                                need_save = 1

                form_opleiding_selected = SelecteerOpleidingForm(request.POST)
                for i in range(len(user_opleiding_modules)):
                    form_buy_module_list.append(BuyModuleForm(request.POST, 
                        auto_id=str(user_opleiding_modules[i].id_module), 
                        prefix=str(user_opleiding_modules[i].id_module))
                    )
                    # dates_form = fill_dates_form(request,modules_user[i], str(modules_user[i].id_module)+'_dates', str(modules_user[i].id_module)+'_dates' )
                    # form_dates_module_list.append(ModulesDatesForm(request.POST, auto_id=str(modules_user[i].id_module)+'_dates', prefix=str(modules_user[i].id_module)+'_dates'))
                    # form_dates_module_list.append(dates_form)

                if need_save == 1 and to_save.buy_module != 1:
                    # for i in data_request:
                    #     for p in range(len(user_opleiding_modules)):
                    #         if i == str(user_opleiding_modules[p].id_module)+'-date':
                    #             name = str(user_opleiding_modules[p].id_module)+'-date'
                    #             date_to_save = data_request[name]
                    module_temp = to_save
                    module_temp.status = 'Bezig'
                    module_temp.buy_module = 1
                    # module_temp.date = date_to_save
                    module_temp.save()
                    user.bank -= module_temp.kosten
                    user.save()
                    need_save = 0

                # data_user = UserProfile.objects.all().get(firstname=firstname, lastname=lastname)
                # modules_user = data_user.modules_set.all()

                # # Determine which modules have status 'Bezig'
                modules_user_bezig = []
                modules_user_voltooid = []
                for i in range(len(user_opleiding_modules)):
                    if user_opleiding_modules[i].status == 'Bezig':
                        modules_user_bezig.append(user_opleiding_modules[i])
                    if user_opleiding_modules[i].status == 'Voltooid':
                        modules_user_voltooid.append(user_opleiding_modules[i])

                baten_flex_bezig = []
                baten_flex_bezig_totaal = 0
                baten_vast_bezig_totaal = 0
                kosten_bezig_totaal = 0

                for i in range(len(modules_user_bezig)):
                    if modules_user_bezig[i].module_type == 'Actief':
                        baten_flex_bezig.append(int(modules_user_bezig[i].factor * 7.5))
                        baten_flex_bezig_totaal += int(modules_user_bezig[i].factor * 7.5)
                        baten_vast_bezig_totaal += int(modules_user_bezig[i].baten_vast)
                        kosten_bezig_totaal += int(modules_user_bezig[i].kosten)
                    if modules_user_bezig[i].module_type == 'Passief':
                        baten_flex_bezig.append('-')
                        baten_vast_bezig_totaal += int(modules_user_bezig[i].baten_vast)
                        kosten_bezig_totaal += int(modules_user_bezig[i].kosten)

                baten_flex_voltooid = []
                baten_flex_voltooid_totaal = 0
                baten_vast_voltooid_totaal = 0
                kosten_voltooid_totaal = 0

                for i in range(len(modules_user_voltooid)):
                    if modules_user_voltooid[i].module_type == 'Actief':
                        baten_flex_voltooid.append(int(modules_user_voltooid[i].factor * modules_user_voltooid[i].cijfer))
                        baten_flex_voltooid_totaal += int(modules_user_voltooid[i].factor * modules_user_voltooid[i].cijfer)
                        baten_vast_voltooid_totaal += int(modules_user_voltooid[i].baten_vast)
                        kosten_voltooid_totaal += int(modules_user_voltooid[i].kosten)
                    if modules_user_voltooid[i].module_type == 'Passief':
                        baten_flex_voltooid.append('-')
                        baten_vast_voltooid_totaal += int(modules_user_voltooid[i].baten_vast)
                        kosten_voltooid_totaal += int(modules_user_voltooid[i].kosten)
                
                baten_bezig_totaal = baten_flex_bezig_totaal + baten_vast_bezig_totaal
                balans_bezig = baten_bezig_totaal - kosten_bezig_totaal
                baten_voltooid_totaal = baten_flex_voltooid_totaal + baten_vast_voltooid_totaal
                balans_voltooid = baten_voltooid_totaal - kosten_voltooid_totaal

                kosten_totaal = kosten_voltooid_totaal + kosten_bezig_totaal
                baten_totaal = baten_voltooid_totaal 

                bank_new = user.bank
                # Determine the position of the buttons
                x_origin = 50.0-2.5
                y_origin = 50.0-2.5
                r = 35
                rad_per = 2*np.pi / 100             # 2 pi / 100 %
                start = .5 * np.pi
                reduce_r = 0.65
                image_size = 100.0
                r_label = 1.2

                #Normalizeren van user wegingen
                data = data_user_selected_opleiding[0]
                weging_tot = data.weging_stud + data.weging_toek + data.weging_soc
                weging_stud_norm = data.weging_stud/float(weging_tot) * 100
                weging_toek_norm = data.weging_toek/float(weging_tot) * 100
                weging_soc_norm = data.weging_soc/float(weging_tot) * 100

                # Button studie toekomst
                theta_stud_toek = start + weging_stud_norm * rad_per
                x_stud_toek = int(r * np.cos(theta_stud_toek) + x_origin) / image_size * 100.0 
                y_stud_toek = int(-1 * r * np.sin(theta_stud_toek) + y_origin) / image_size * 100.0 

                # Button toekomst student
                theta_toek_soc = start + (weging_toek_norm + weging_stud_norm) * rad_per
                x_toek_soc = int(r * np.cos(theta_toek_soc) + x_origin)/ image_size * 100.0 
                y_toek_soc = int(-1 * r * np.sin(theta_toek_soc) + y_origin) / image_size * 100.0 

                # Button student studie
                theta_soc_stud = start
                x_soc_stud = int(r * np.cos(theta_soc_stud) + x_origin) / image_size * 100.0 
                y_soc_stud = int( -1* r * np.sin(theta_soc_stud) +  y_origin) / image_size * 100.0 

                if weging_stud_norm < 10.0 and weging_stud_norm > 7.0:
                    reduce_r_stud = 0.6
                    # Button studie 1
                    theta_stud1 = start + (weging_stud_norm * rad_per * 0.5)
                    x_stud1 = int(reduce_r_stud * reduce_r * r * np.cos(theta_stud1) + x_origin) / image_size * 100 
                    y_stud1 = int(reduce_r_stud * reduce_r * -1 * r * np.sin(theta_stud1) + y_origin) / image_size * 100 

                    # Button studie 2
                    theta_stud2 = start + (weging_stud_norm * rad_per * 0.5) 
                    x_stud2 = int(reduce_r * r * np.cos(theta_stud2) + x_origin) / image_size * 100.0 
                    y_stud2 = int(reduce_r * -1 * r * np.sin(theta_stud2) + y_origin) / image_size * 100.0 
                elif weging_stud_norm < 7.0 :
                    reduce_r_stud = 0.6
                    # Button studie 1
                    theta_stud1 = start + (weging_stud_norm * rad_per * 0.5)
                    x_stud1 = int(reduce_r_stud * reduce_r * r * np.cos(theta_stud1) + x_origin) / image_size * 100 + 2.0
                    y_stud1 = int(reduce_r_stud * reduce_r * -1 * r * np.sin(theta_stud1) + y_origin) / image_size * 100 + 2.0

                    # Button studie 2
                    theta_stud2 = start + (weging_stud_norm * rad_per * 0.5) 
                    x_stud2 = int(reduce_r * r * np.cos(theta_stud2) + x_origin) / image_size * 100.0 + 2.0
                    y_stud2 = int(reduce_r * -1 * r * np.sin(theta_stud2) + y_origin) / image_size * 100.0 + 2.0
                else:
                    # Button studie 1
                    theta_stud1 = start + (weging_stud_norm * rad_per * 0.3)
                    x_stud1 = int(reduce_r * r * np.cos(theta_stud1) + x_origin) / image_size * 100 
                    y_stud1 = int(reduce_r * -1 * r * np.sin(theta_stud1) + y_origin) / image_size * 100 

                    # Button studie 2
                    theta_stud2 = start + (weging_stud_norm * rad_per * 0.7) 
                    x_stud2 = int(reduce_r * r * np.cos(theta_stud2) + x_origin) / image_size * 100.0 
                    y_stud2 = int(reduce_r * -1 * r * np.sin(theta_stud2) + y_origin) / image_size * 100.0 

                # Button studie
                theta_stud = start + (weging_stud_norm * rad_per * 0.5)
                x_stud = int(reduce_r * r * np.cos(theta_stud) + x_origin)  / image_size * 100.0 
                y_stud = int(reduce_r * -1 * r * np.sin(theta_stud) + y_origin) / image_size * 100.0 

                x_stud_label = int(r_label * r * np.cos(theta_stud) + x_origin)  / image_size * 100.0 
                y_stud_label = int(r_label * -1 * r * np.sin(theta_stud) + y_origin) / image_size * 100.0 

                # Button toekomst
                theta_toek = start + weging_stud_norm * rad_per + (weging_toek_norm * rad_per * 0.5)
                x_toek = int(reduce_r * r * np.cos(theta_toek) + x_origin) / image_size * 100.0
                y_toek = int(reduce_r * -1 * r * np.sin(theta_toek) + y_origin) / image_size * 100.0 

                x_toek_label = int(r * r_label * np.cos(theta_toek) + x_origin) / image_size * 100.0
                y_toek_label = int(r * r_label * -1 * np.sin(theta_toek) + y_origin) / image_size * 100.0 


                # Button student
                theta_soc = start + (weging_toek_norm + weging_stud_norm) * rad_per + (weging_soc_norm * 0.5 * rad_per)
                x_soc = int(reduce_r * r * np.cos(theta_soc) + x_origin) / image_size * 100.0 
                y_soc = int(-1 * reduce_r * r * np.sin(theta_soc) + y_origin) / image_size * 100.0 

                # username = request.user.username
                # firstname = request.user.userprofile.firstname
                # lastname = request.user.userprofile.lastname
                # bank = request.user.userprofile.bank
                graphic = MakePieChart(request)

                #Normalizing expeience
                exp_user_stud_norm = data.exp_stud / 1000.0 * 100
                exp_user_soc_norm = data.exp_soc / 1000.0 * 100
                exp_user_toek_norm = data.exp_toek / 1000.0 * 100
                exp_user_totaal_norm = exp_user_stud_norm + exp_user_soc_norm + exp_user_toek_norm

                # modules_user = UserProfile.objects.all().get(firstname=firstname, lastname=lastname)
                # modules = modules_user.modules_set.all()
                username = str(Gebruiker.user)
                user = data_user_selected_opleiding[0]
                bank = data_user_selected_opleiding[0].bank
                form = 'main/loggedin.html' 

                
                response = {'Gebruiker': Gebruiker,
                            'user_selected_opleiding':user_selected_opleiding,
                            'data_user_opleiding':data_user_opleiding,
                            'data_user_selected_opleiding':data_user_selected_opleiding,
                            'data_user_selected_opleiding_modules':data_user_selected_opleiding_modules,
                            # 'user_modules_opleiding_selected': user_modules_opleiding_selected,
                            # 'full_name': username, #'graphic': graphic,
                            'bank': bank,
                            # 'firstname':firstname, 'lastname':lastname, 
                            'user':user,
                            'username': username,
                            'x_soc_stud':  x_soc_stud, 'y_soc_stud': y_soc_stud,
                            'x_stud_toek':  x_stud_toek, 'y_stud_toek': y_stud_toek, 
                            'x_toek_soc':  x_toek_soc, 'y_toek_soc': y_toek_soc,
                            'x_stud': x_stud, 'y_stud': y_stud,
                            'x_stud1': x_stud1, 'y_stud1': y_stud1,
                            'x_stud2': x_stud2, 'y_stud2': y_stud2,
                            'x_toek': x_toek, 'y_toek': y_toek, 'x_toek_label':x_toek_label, 'y_toek_label':y_toek_label, 
                            'x_soc': x_soc, 'y_soc': y_soc,
                            'weging_stud_norm':weging_stud_norm, 'weging_toek_norm':weging_toek_norm, 'weging_soc_norm':weging_soc_norm,
                            # 'weging_stud':Gebruiker.weging_stud,
                            # 'weging_tot':weging_tot,
                            'modules': modules,
                            'data_request':data_request,
                            'form_opleiding_selected': form_opleiding_selected,
                            # 'data_user':data_user,
                            # 'form_buy_module_list':form_buy_module_list,
                            # 'to_save':to_save,
                            'baten_flex_bezig':baten_flex_bezig,
                            'baten_flex_voltooid':baten_flex_voltooid,
                            # 'modules_user_bezig':modules_user_bezig,
                            'kosten_totaal': kosten_totaal, 'baten_totaal':baten_totaal,
                            'exp_user_stud_norm': exp_user_stud_norm, 'exp_user_soc_norm':exp_user_soc_norm, 'exp_user_toek_norm':exp_user_toek_norm,
                            # 'exp_user_totaal_norm':exp_user_totaal_norm,
                            # 'data_request':data_request,
                }
                for i in range(len(form_buy_module_list)):
                    response['buy_'+str(i)] = form_buy_module_list[i]
                    # response['dates_'+str(i)] = form_dates_module_list[i]

                return render(request, form, response)
        else:
            page_not_permitted(request)
            return HttpResponseRedirect('/page_not_permitted')


def logout(request):
        auth.logout(request)
        return HttpResponseRedirect('/login')

def MakePieChart(request):
        # make a square figure and axes
        fig, ax = plt.subplots(1, figsize=(9,9))

        # pylab.figure(1, figsize=(6, 6))
        username = request.user.username

        # The slices will be ordered and plotted counter-clockwise.
        Gebruiker = request.user.userprofile_general
        user_selected_opleiding = Gebruiker.opleiding_selected
        data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker, opleiding=user_selected_opleiding)[0]

        #Normalizeren van user wegingen
        weging_tot = data_user_selected_opleiding.weging_stud + data_user_selected_opleiding.weging_toek + data_user_selected_opleiding.weging_soc
        weging_stud_norm = data_user_selected_opleiding.weging_stud/float(weging_tot) #* 100
        weging_toek_norm = data_user_selected_opleiding.weging_toek/float(weging_tot) #* 100
        weging_soc_norm = data_user_selected_opleiding.weging_soc/float(weging_tot) #* 100

        fracs = [weging_stud_norm, weging_toek_norm, weging_soc_norm]
        colors = ['#eea236', '#4dbadb', '#d44844']

        ax.pie(fracs,
                  colors=colors,
                  shadow=False,
                  startangle=90)

        plt.draw()
        plt.savefig('./main/static/main/user_piecharts/' + username + str(user_selected_opleiding) + '.png', bbox_inches='tight')
        plt.close()
        string = 'main/user_piecharts/' + username + str(user_selected_opleiding) + '.png'

        return string

def weging(request):
    Gebruiker = request.user.userprofile_general
    user_selected_opleiding = Gebruiker.opleiding_selected
    data_user_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker)
    data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker, opleiding=str(user_selected_opleiding))
    user = data_user_selected_opleiding[0]

    # Selecteer opleiding
    data_request = 0
    if request.method == "POST":
        data_request = request.POST
        if request.POST.get('opleiding_selected'):
            Gebruiker.opleiding_selected = request.POST['opleiding_selected']
            Gebruiker.save();

    user_selected_opleiding = Gebruiker.opleiding_selected
    data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=Gebruiker, opleiding=str(user_selected_opleiding))
    user = data_user_selected_opleiding[0]
    form_opleiding_selected = SelecteerOpleidingForm(request.POST)

    if Gebruiker.is_student == True :
        firstname = Gebruiker.firstname
        lastname = Gebruiker.lastname
        opleiding_selected = Gebruiker.opleiding_selected    

        form_userprofile_opleiding = UserProfileOpleidingForm(request.POST)
        weging_stud = user.weging_stud
        weging_toek = user.weging_toek
        weging_soc = user.weging_soc

        if request.method == "POST":
            if request.POST.get('weging_soc') and request.POST.get('weging_stud') and request.POST.get('weging_toek'):
                data_request = request.POST
                # form_userprofile_opleiding = UserProfileOpleidingForm() #request.POST) #, instance=Gebruiker)

                if form_userprofile_opleiding.is_valid():
                    user.weging_stud = form_userprofile_opleiding['weging_stud'].value()
                    user.weging_toek = form_userprofile_opleiding['weging_toek'].value()
                    user.weging_soc  = form_userprofile_opleiding['weging_soc'].value()
                    user.save()
                    MakePieChart(request)
                    return HttpResponseRedirect('/loggedin')

                else:
                    form = 'main/weging.html'
                    response = {'firstname':firstname, 'lastname':lastname,
                        'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
                        'form_userprofile_opleiding':form_userprofile_opleiding,
                        'data_request':data_request, 'Gebruiker':Gebruiker, 
                        'data_user_opleiding':data_user_opleiding,
                        'form_opleiding_selected':form_opleiding_selected,
                        }

                    return render(request, form, response)
            else:
                form = 'main/weging.html'
                response = {'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
                    'form_userprofile_opleiding':form_userprofile_opleiding,
                    'data_request':data_request, 'Gebruiker':Gebruiker, 
                    'data_user_opleiding':data_user_opleiding,
                    'form_opleiding_selected':form_opleiding_selected,
                    }

                return render(request, form, response)

        else:
            form = 'main/weging.html'
            response = {'Gebruiker':Gebruiker,
                'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
                'form_userprofile_opleiding':form_userprofile_opleiding,
                'data_request':data_request, 'data_user_opleiding': data_user_opleiding,
                'form_opleiding_selected':form_opleiding_selected,
                }

            return render(request, form, response)
    else:
        page_not_permitted(request)
        return HttpResponseRedirect('/page_not_permitted')

def docent(request):
    form = "main/docent.html"
    form_userprofile = SelecteerStudentForm()

    teacher = request.user.userprofile_general

    if teacher.is_teacher == True :
        if request.method == "POST":
            firstname = request.POST.get('firstname', "")
            lastname = request.POST.get('lastname', "")
            data_request = request.POST
            form_opleiding_selected = SelecteerOpleidingForm(request.POST)

            if firstname != "" and lastname != "":
                message_found = "True"

                all_users = UserProfile_General.objects.all()
                user_in = False 
                user_is_teacher = False
                for i in range(len(all_users)):
                    user = all_users[i]
                    if user.firstname.lower() == firstname.lower() and user.lastname.lower() == lastname.lower():
                        user_in = True
                        if user.is_teacher:
                            user_is_teacher = True;
                        user_searched = user

                if user_in == False:
                    message_not_found = "Geen match gevonden. Probeer opnieuw!"
                    error = "True"

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                                'error':error, 'all_users':all_users, 'teacher':teacher,
                    }
                    return render(request, form, response)

                if user_in == True and user_is_teacher == True:
                    message_not_found = "Geen zoekresultaten mogelijk voor een docent!"
                    error = "True"

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                                'error':error, 'all_users':all_users, 'teacher':teacher,
                    }
                    return render(request, form, response)

                elif user_in == True and user_is_teacher == False:
                    message_found = "True"
                    error = "True"

                    form_userprofile = SelecteerStudentForm(request.POST)
                    if form_userprofile.is_valid():
                        temp = form_userprofile.save(commit=False)
                        temp.firstname = firstname
                        temp.lastname = lastname
                        # temp.save()
                        opslaan = "Succes"
                    else:
                        opslaan = "Failure"

                    data_user = UserProfile_General.objects.filter(firstname=firstname, lastname=lastname)[0]
                    data_user_object = UserProfile_General.objects.filter(firstname=firstname, lastname=lastname)
                    user_opleiding_selected = data_user.opleiding_selected
                    data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=data_user_object, opleiding=user_opleiding_selected)
                    data_user_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=data_user_object)
                    modules_user = Modules.objects.filter(username=str(data_user), userprofile_opleiding=data_user_selected_opleiding)

                    data_request = request.POST
                    if request.method == "POST":
                        if request.POST.get('opleiding_selected'):
                            teacher_selected = request.POST['opleiding_selected']
                            data_user_selected_opleiding = UserProfile_Opleiding.objects.filter(userprofile_general=data_user_object, opleiding=teacher_selected)
                            modules_user = Modules.objects.filter(username=str(data_user), userprofile_opleiding=data_user_selected_opleiding)
                        else:
                            teacher_selected = user_opleiding_selected


                    index_modules_user_pending = []
                    modules_user_pending = []
                    index_modules_user_complete = []
                    modules_user_complete = []
                    index_modules_user_notdone = []
                    modules_user_notdone = []

                    for i in range(len(modules_user)):
                        if modules_user[i].status == 'Bezig':
                            modules_user_pending.append(modules_user[i])
                            index_modules_user_pending.append(i)
                        if modules_user[i].status == 'Voltooid':
                            modules_user_complete.append(modules_user[i])
                            index_modules_user_complete.append(i)
                        if modules_user[i].status == 'Niet gedaan':
                            modules_user_notdone.append(modules_user[i])
                            index_modules_user_notdone.append(i)

                    form_modules_actief = []
                    form_modules_passief = []
                    form_modules_cijfer = [] #cijfer uit het form
                    form_modules_naam = []
                    for i in range(len(modules_user_pending)):
                        if modules_user_pending[i].module_type == "Actief":
                            form_modules_actief.append(ModuleForm(request.POST, auto_id="form_modules_actief"+str(i), prefix=str(modules_user_pending[i].id_module)))

                    form_modules_cijfer_clean = []
                    for i in range(len(form_modules_actief)):
                        form_temp = form_modules_actief[i]
                        if form_modules_actief[i]['cijfer'].value() == None:
                            form_modules_cijfer.append(0)
                        if form_modules_actief[i]['cijfer'].value() == "":
                            form_modules_cijfer.append(0)
                        if form_modules_actief[i]['cijfer'].value() == 0:
                            form_modules_cijfer.append(0)
                        else:
                            form_modules_cijfer.append(form_modules_actief[i]['cijfer'].value())

                    for i in range(len(form_modules_cijfer)):
                        if str(form_modules_cijfer[i]) != "None" and str(form_modules_cijfer[i]) != "":
                            form_modules_cijfer_clean.append(int(form_modules_cijfer[i]))

                    for i in range(len(modules_user_pending)):
                        if modules_user_pending[i].module_type == 'Passief' :
                            form_modules_passief.append( ModuleForm(request.POST, auto_id="form_modules_passief"+str(i), prefix=str(modules_user_pending[i].id_module) ) )          


                    #determine which modules needs to be saved
                    to_save = 0
                    user_modules_cijfer = [] #cijfer van de user voor elke module
                    for i in data_request:
                        for p in range(len(modules_user_pending)):
                            if i == modules_user_pending[p].id_module:
                                to_save = modules_user_pending[p].id_module

                    # selecting correct user data
                    username = UserProfile_Opleiding.objects.filter(userprofile_general=data_user_object, opleiding=user_opleiding_selected)[0]

                    cijfer_to_save = 0
                    for i in range(len(modules_user_pending)) :
                        if modules_user_pending[i].id_module == to_save:
                            module_temp = modules_user_pending[i]
                            if module_temp.module_type == 'Actief':
                                index = str(to_save+'-cijfer')
                                cijfer_to_save = data_request[index]
                                module_temp.cijfer = cijfer_to_save
                                module_temp.status = 'Voltooid'
                                module_temp.save()
                                if module_temp.gebied == 'studie':
                                    username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'studietoekomst':
                                    username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                    username.exp_toek += module_temp.experience_vast+ int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'toekomst':
                                    username.exp_toek += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'sociaaltoekomst':
                                    username.exp_toek += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                    username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'sociaal':
                                    username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'studiesociaal':
                                    username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                    username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                username.bank += int(int(module_temp.cijfer) * module_temp.factor + int(module_temp.baten_vast))
                                username.save()
                            if module_temp.module_type == 'Passief':
                                index = str(to_save+'-cijfer')
                                module_temp.status = 'Voltooid'
                                module_temp.save()
                                
                                if module_temp.gebied == 'studie':
                                    username.exp_stud += module_temp.experience_vast
                                if module_temp.gebied == 'studietoekomst':
                                    username.exp_stud += module_temp.experience_vast
                                    username.exp_toek += module_temp.experience_vast
                                if module_temp.gebied == 'toekomst':
                                    username.exp_toek += module_temp.experience_vast
                                if module_temp.gebied == 'sociaaltoekomst':
                                    username.exp_toek += module_temp.experience_vast
                                    username.exp_soc += module_temp.experience_vast
                                if module_temp.gebied == 'sociaal':
                                    username.exp_soc += module_temp.experience_vast
                                if module_temp.gebied == 'studiesociaal':
                                    username.exp_soc += module_temp.experience_vast
                                    username.exp_stud += module_temp.experience_vast

                                username.bank += module_temp.baten_vast
                                username.exp_tot = username.exp_stud + username.exp_soc + username.exp_toek
                                username.save()

                    # response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 
                    #             'data_request':data_request, 'message_found': message_found,
                    #             'data_user':data_user, 'user_opleiding_selected':user_opleiding_selected,'data_user_selected_opleiding':data_user_selected_opleiding,
                    #             'error':error, 'all_users':all_users,
                    #             'modules_user':modules_user,
                    # }
                    
                    #Update status list
                    modules_user_pending = []
                    modules_user_complete = []
                    modules_user_notdone = []
                    index_actief = []
                    for i in range(len(modules_user)):
                        if modules_user[i].status == 'Bezig':
                            modules_user_pending.append(modules_user[i])
                            index_modules_user_pending.append(i)
                            if modules_user[i].module_type == 'Actief' :
                                index_actief.append(i)
                        if modules_user[i].status == 'Voltooid':
                            modules_user_complete.append(modules_user[i])
                            index_modules_user_complete.append(i)
                        if modules_user[i].status == 'Niet gedaan':
                            modules_user_notdone.append(modules_user[i])
                            index_modules_user_notdone.append(i)

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 
                        'message_found':message_found,
                        'data_user':data_user, 
                        'data_user_opleiding':data_user_opleiding,
                        'modules_user':modules_user, #'modules_user_cijfer':modules_user_cijfer, 
                        'modules_user_pending':modules_user_pending,
                        'modules_user_complete':modules_user_complete,
                        'modules_user_notdone':modules_user_notdone,
                        'form_opleiding_selected':form_opleiding_selected,
                        'teacher_selected':teacher_selected,
                        # 'form_modules_cijfer':form_modules_cijfer,
                        # 'user_modules_cijfer':user_modules_cijfer,
                        # 'form_modules_naam':form_modules_naam,
                        'form_modules_actief':form_modules_actief,
                        'form_modules_cijfer_clean':form_modules_cijfer_clean,
                        # 'username':username,
                        'teacher':teacher,
                        'data_request':data_request,
                    }
                    for i in range(len(form_modules_actief)) :
                        response['form_modules_actief'+str(i)] = form_modules_actief[i]

                    form_modules_cijfer_clean = []
                    return render(request, form, response)

                elif user_in == True and user_searched.is_teacher == True :
                    message_not_found = "Voer een valide naam in!"
                    error = "True"
                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                                'error':error,'teacher':teacher,
                    }

            else:
                message_not_found = "Voer een valide naam in!"
                error = "True"
                response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                            'error':error,'teacher':teacher,
                }

                return render(request, form, response)

        else:
            response = {'form_userprofile':form_userprofile,'teacher':teacher,
            }

            return render(request, form, response)

    else:
        page_not_permitted(request)
        return HttpResponseRedirect('/page_not_permitted')

def page_not_permitted(request):
    form = 'main/page_not_permitted.html'
    Gebruiker = request.user.userprofile_general
    response = {'Gebruiker':Gebruiker}
    return render(request, form, response )
'''
def MakePieChart(request):
        # make a square figure and axes
        fig, ax = plt.subplots(1, figsize=(9,9))

        # pylab.figure(1, figsize=(6, 6))
        username = request.user.username

        # The slices will be ordered and plotted counter-clockwise.
        Gebruiker = request.user.userprofile

        #Normalizeren van user wegingen
        weging_tot = Gebruiker.weging_stud + Gebruiker.weging_toek + Gebruiker.weging_soc
        weging_stud_norm = Gebruiker.weging_stud/float(weging_tot) #* 100
        weging_toek_norm = Gebruiker.weging_toek/float(weging_tot) #* 100
        weging_soc_norm = Gebruiker.weging_soc/float(weging_tot) #* 100

        fracs = [weging_stud_norm, weging_toek_norm, weging_soc_norm]
        colors = ['#eea236', '#4dbadb', '#d44844']

        ax.pie(fracs,
                  colors=colors,
                  shadow=False,
                  startangle=90)

        plt.draw()
        plt.savefig('./main/static/main/user_piecharts/' + username + '.png', bbox_inches='tight')
        plt.close()
        string = 'main/user_piecharts/' + username + '.png'

        return string

def weging(request):
    Gebruiker = request.user.userprofile

    if Gebruiker.is_student == True :
        firstname = Gebruiker.firstname
        lastname = Gebruiker.lastname    

        if request.method == "POST":
            form_userprofile = UserProfileForm(request.POST, instance=Gebruiker)

            weging_stud = form_userprofile['weging_stud'].value()
            weging_toek = form_userprofile['weging_toek'].value()
            weging_soc  = form_userprofile['weging_soc'].value()

            if form_userprofile.is_valid():
                form_userprofile.save();
                MakePieChart(request)
                return HttpResponseRedirect('/#loggedin')

            else:
                form = 'main/weging.html'
                response = {'firstname':firstname, 'lastname':lastname,
                    'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
                    'form_userprofile':form_userprofile,
                    }

                return render(request, form, response)

        else:
            form_userprofile = UserProfileForm()
            weging_stud = Gebruiker.weging_stud
            weging_toek = Gebruiker.weging_toek
            weging_soc = Gebruiker.weging_soc

            form = 'main/weging.html'
            response = {'firstname':firstname, 'lastname':lastname,
                'Gebruiker':request.user.userprofile,
                'weging_stud':weging_stud, 'weging_toek':weging_toek, 'weging_soc':weging_soc,
                'form_userprofile':form_userprofile,
                }

            return render(request, form, response)
    else:
        page_not_permitted(request)
        return HttpResponseRedirect('/page_not_permitted')

previous_search = []
previous_username = []
def docent(request):
    form = "main/docent.html"
    form_userprofile = UserProfileForm()

    teacher = request.user.userprofile

    if teacher.is_teacher == True :
        if request.method == "POST":
            firstname = request.POST.get('firstname', "")
            lastname = request.POST.get('lastname', "")
            data_request = request.POST

            if firstname != "" and lastname != "":
                message_found = "True"

                all_users = UserProfile.objects.all()
                user_in = False 
                user_is_teacher = False
                for i in range(len(all_users)):
                    user = all_users[i]
                    if user.firstname.lower() == firstname.lower() and user.lastname.lower() == lastname.lower():
                        user_in = True
                        if user.is_teacher:
                            user_is_teacher = True;
                        user_searched = user

                if user_in == False:
                    message_not_found = "Geen match gevonden. Probeer opnieuw!"
                    error = "True"

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                    			'error':error, 'all_users':all_users,
                    }
                    return render(request, form, response)

                if user_in == True and user_is_teacher == True:
                    message_not_found = "Geen zoekresultaten mogelijk voor een docent!"
                    error = "True"

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                                'error':error, 'all_users':all_users,
                    }
                    return render(request, form, response)

                elif user_in == True and user_is_teacher == False:
                    data_user = UserProfile.objects.all().get(firstname=firstname, lastname=lastname)
                    modules_user = data_user.modules_set.all()

                    data_request = request.POST

                    firstname = data_user.firstname
                    lastname = data_user.lastname

                    form_userprofile = UserProfileForm(request.POST, instance=data_user)
                    if form_userprofile.is_valid():
                        temp = form_userprofile.save(commit=False)
                        temp.firstname = firstname
                        temp.lastname = lastname
                        temp.weging_stud = data_user.weging_stud
                        temp.weging_toek = data_user.weging_toek
                        temp.weging_soc = data_user.weging_soc
                        # temp.save()
                        opslaan = "Succes"
                    else:
                        opslaan = "Failure"

                    index_modules_user_pending = []
                    modules_user_pending = []
                    index_modules_user_complete = []
                    modules_user_complete = []
                    index_modules_user_notdone = []
                    modules_user_notdone = []

                    for i in range(len(modules_user)):
                        if modules_user[i].status == 'Bezig':
                            modules_user_pending.append(modules_user[i])
                            index_modules_user_pending.append(i)
                        if modules_user[i].status == 'Voltooid':
                        	modules_user_complete.append(modules_user[i])
                        	index_modules_user_complete.append(i)
                        if modules_user[i].status == 'Niet gedaan':
                        	modules_user_notdone.append(modules_user[i])
                        	index_modules_user_notdone.append(i)

                    form_modules_actief = []
                    form_modules_passief = []
                    form_modules_cijfer = [] #cijfer uit het form
                    form_modules_naam = []
                    for i in range(len(modules_user_pending)):
                        if modules_user_pending[i].module_type == "Actief":
                        	form_modules_actief.append(ModuleForm(request.POST, auto_id="form_modules_actief"+str(i), prefix=str(modules_user_pending[i].id_module)))

                    form_modules_cijfer_clean = []
                    for i in range(len(form_modules_actief)):
                    	form_temp = form_modules_actief[i]
                    	if form_modules_actief[i]['cijfer'].value() == None:
                    		form_modules_cijfer.append(0)
                    	if form_modules_actief[i]['cijfer'].value() == "":
                    		form_modules_cijfer.append(0)
                    	if form_modules_actief[i]['cijfer'].value() == 0:
                    		form_modules_cijfer.append(0)
                    	else:
                    		form_modules_cijfer.append(form_modules_actief[i]['cijfer'].value())

                    for i in range(len(form_modules_cijfer)):
                    	if str(form_modules_cijfer[i]) != "None" and str(form_modules_cijfer[i]) != "":
                    		form_modules_cijfer_clean.append(int(form_modules_cijfer[i]))

                    for i in range(len(modules_user_pending)):
                    	if modules_user_pending[i].module_type == 'Passief' :
                    		form_modules_passief.append( ModuleForm(request.POST, auto_id="form_modules_passief"+str(i), prefix=str(modules_user_pending[i].id_module) ) )         	

                    #determine which modules needs to be saved
                    to_save = 0
                    user_modules_cijfer = [] #cijfer van de user voor elke module
                    for i in data_request:
                    	for p in range(len(modules_user_pending)):
                    		if i == modules_user_pending[p].id_module:
                    			to_save = modules_user_pending[p].id_module

                    # Save changes of the correct module
                    username = UserProfile.objects.all().get(firstname=firstname, lastname=lastname)
                    modules_user = username.modules_set.all()
                    cijfer_to_save = 0
                    for i in range(len(modules_user_pending)) :
                        if modules_user_pending[i].id_module == to_save:
                            module_temp = modules_user_pending[i]
                            if module_temp.module_type == 'Actief':
                                index = str(to_save+'-cijfer')
                                cijfer_to_save = data_request[index]
                                module_temp.cijfer = cijfer_to_save
                                module_temp.status = 'Voltooid'
                                module_temp.save()
                                if module_temp.gebied == 'studie':
                                	username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'studietoekomst':
                                	username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                	username.exp_toek += module_temp.experience_vast+ int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'toekomst':
                                	username.exp_toek += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'sociaaltoekomst':
                                	username.exp_toek += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                	username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'sociaal':
                                	username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                if module_temp.gebied == 'studiesociaal':
                                	username.exp_soc += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                	username.exp_stud += module_temp.experience_vast + int(module_temp.cijfer) * int(module_temp.factor)
                                username.bank += int(int(module_temp.cijfer) * module_temp.factor + int(module_temp.baten_vast))
                                username.save()
                            if module_temp.module_type == 'Passief':
                                index = str(to_save+'-cijfer')
                                module_temp.status = 'Voltooid'
                                module_temp.save()
                                
                                if module_temp.gebied == 'studie':
                                	username.exp_stud += module_temp.experience_vast
                                if module_temp.gebied == 'studietoekomst':
                                	username.exp_stud += module_temp.experience_vast
                                	username.exp_toek += module_temp.experience_vast
                                if module_temp.gebied == 'toekomst':
                                	username.exp_toek += module_temp.experience_vast
                                if module_temp.gebied == 'sociaaltoekomst':
                                	username.exp_toek += module_temp.experience_vast
                                	username.exp_soc += module_temp.experience_vast
                                if module_temp.gebied == 'sociaal':
                                	username.exp_soc += module_temp.experience_vast
                                if module_temp.gebied == 'studiesociaal':
                                	username.exp_soc += module_temp.experience_vast
                                	username.exp_stud += module_temp.experience_vast

                                username.bank += module_temp.baten_vast
                                username.exp_tot = username.exp_stud + username.exp_soc + username.exp_toek
                                username.save()

                    #Update status list
                    modules_user_pending = []
                    modules_user_complete = []
                    modules_user_notdone = []
                    index_actief = []
                    for i in range(len(modules_user)):
                    	if modules_user[i].status == 'Bezig':
                    		modules_user_pending.append(modules_user[i])
                    		index_modules_user_pending.append(i)
                    		if modules_user[i].module_type == 'Actief' :
                    			index_actief.append(i)
                    	if modules_user[i].status == 'Voltooid':
                    		modules_user_complete.append(modules_user[i])
                    		index_modules_user_complete.append(i)
                    	if modules_user[i].status == 'Niet gedaan':
                    		modules_user_notdone.append(modules_user[i])
                    		index_modules_user_notdone.append(i)

                    response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 
                        'message_found':message_found,
                        'data_user':data_user, 
                        'modules_user':modules_user, #'modules_user_cijfer':modules_user_cijfer, 
                        'modules_user_pending':modules_user_pending,
                        'modules_user_complete':modules_user_complete,
                        'modules_user_notdone':modules_user_notdone,
                        'form_modules_cijfer':form_modules_cijfer,
                        'user_modules_cijfer':user_modules_cijfer,
                        'form_modules_naam':form_modules_naam,
                        'form_modules_actief':form_modules_actief,
                        'form_modules_cijfer_clean':form_modules_cijfer_clean,
                        'username':username,
                        'teacher':teacher,
                        'data_request':data_request,
                    }
                    for i in range(len(form_modules_actief)) :
                        response['form_modules_actief'+str(i)] = form_modules_actief[i]

                    form_modules_cijfer_clean = []

                    return render(request, form, response)

                # elif user_in == True and user_searched.is_teacher == True :
                #     message_not_found = "Voer een valide naam in!"
                #     error = "True"
                #     response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                #                 'error':error,'teacher':teacher,
                #     }

            else:
                message_not_found = "Voer een valide naam in!"
                error = "True"
                response = {'form_userprofile':form_userprofile, 'firstname':firstname, 'lastname': lastname, 'data_request':data_request, 'message_not_found': message_not_found,
                			'error':error,'teacher':teacher,
                }

                return render(request, form, response)

        else:
            response = {'form_userprofile':form_userprofile,'teacher':teacher,
            }

            return render(request, form, response)

    else:
        page_not_permitted(request)
        return HttpResponseRedirect('/page_not_permitted')

def vragen(request):
        Gebruiker = request.user.userprofile

        if Gebruiker.is_student == True:

            firstname = Gebruiker.firstname
            lastname = Gebruiker.lastname
            form = 'main/vragen.html'
            import time
            localtime = time.localtime(time.time())
            year = localtime[0]
            month = localtime[1]
            day = localtime[2]
            hour = localtime[3]+2
            minute = localtime[4] 
            second = localtime[5]


            question_form = []
            for i in range(12):
                    question_form.append(QuestionForm(prefix=str(i), auto_id='id_%s'))

            if request.method == "POST":
                    A = Gebruiker
                    Aquest = A.questions_set.all()
                    for i in range(12):
                            question_data = QuestionForm(request.POST, prefix=str(i))
                            temp = Questions.objects.create(
                                    question =  question_data['question'].value(),
                                    answers =  question_data['answers'].value(),
                                    gebied =  question_data['gebied'].value(),
                                    userprofile = A,
                                    naam_question_gebruiker = str(A)+'_q'+str(i)+'_'+str(year)+'-'+str(month)+'-'+str(day)+'_'+str(hour)+':'+str(minute)+':'+str(second),
                                    )
                            temp.save()
                            A.questions_set.add(temp)
                    return HttpResponseRedirect('/weging')

            stud_lijst = Gebruiker.questions_set.all().filter(gebied="studie")
            stud_lijst = stud_lijst.order_by('-timestamp')[:4]
            toek_lijst = Gebruiker.questions_set.all().filter(gebied="toekomst")
            toek_lijst = toek_lijst.order_by('-timestamp')[:4]
            soc_lijst = Gebruiker.questions_set.all().filter(gebied="sociaal")
            soc_lijst = soc_lijst.order_by('-timestamp')[:4]

            response = {'stud_lijst': stud_lijst,
                        'toek_lijst': toek_lijst,
                        'soc_lijst': soc_lijst,
                        'firstname': firstname,
                        'lastname': lastname,
                        'localtime':localtime,
                        }
            i = 0
            for items in question_form:
                    response['qform' + str(i)] = items
                    i += 1

            return render(request, form, response)

        else:
            page_not_permitted(request)
            return HttpResponseRedirect('/page_not_permitted')

def pdf_export(request):
    Gebruiker = request.user.userprofile
    if Gebruiker.is_student == True:
        firstname = Gebruiker.firstname
        lastname = Gebruiker.lastname
        form = 'main/pdf_export.html'
        user = Gebruiker

        modules_user = user.modules_set.all()

        temp = ExportPDFForm()

        exp_user_stud_norm = Gebruiker.exp_stud / 1000.0 * 100
        exp_user_soc_norm = Gebruiker.exp_soc / 1000.0 * 100
        exp_user_toek_norm = Gebruiker.exp_toek / 1000.0 * 100
        exp_user_totaal_norm = exp_user_stud_norm + exp_user_soc_norm + exp_user_toek_norm
        success = 'success'
        pdf_export_selector = 'True'

        data_request = 0 
        if request.method == "POST":
            temp = ExportPDFForm(request.POST)
            data_request = request.POST

            html_template = get_template('main/pdf_export_frame.html')
            rendered_html = html_template.render({'firstname':firstname, 'lastname':lastname, 'data_request':data_request,
                    'exp_user_stud_norm': exp_user_stud_norm, 'exp_user_soc_norm':exp_user_soc_norm, 'exp_user_toek_norm':exp_user_toek_norm,
                    'exp_user_totaal_norm':exp_user_totaal_norm, 'user':user, 'modules_user':modules_user,'pdf_export_selector':pdf_export_selector,
                    'exp_stud':Gebruiker.exp_stud, 'exp_toek':Gebruiker.exp_toek, 'exp_soc':Gebruiker.exp_soc, 'exp_tot':Gebruiker.exp_tot,
                        }).encode(encoding="UTF-8")

            pdf_file = HTML(string=rendered_html,base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS('main/static/main/css/css_pdf_export.css')])

            filename = 'export_'+str(firstname)+'_'+str(lastname)+'.pdf'
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

            return response

        response = {'firstname':firstname, 'lastname':lastname, 'data_request':data_request, 'form_pdf_export':temp,
                    'exp_user_stud_norm': exp_user_stud_norm, 'exp_user_soc_norm':exp_user_soc_norm, 'exp_user_toek_norm':exp_user_toek_norm,
                    'exp_user_totaal_norm':exp_user_totaal_norm, 'user':user, 'modules_user':modules_user,'success':success,
        }

        return render(request, form, response)
    else:
        page_not_permitted(request)
        return HttpResponseRedirect('/page_not_permitted')
    
def page_not_permitted(request):
    form = 'main/page_not_permitted.html'
    Gebruiker = request.user.userprofile
    response = {'Gebruiker':Gebruiker}
    return render(request, form, response )

def fill_dates_form(request, module, auto_id_given, prefix_given):
    CHOICES = (
        ('date1', str(module.date1)),
        ('date2', str(module.date2)),
    )
    # CHOICES = [ ('date1', 'date1'),('date2', 'date2')]
    form_dates = ModulesDatesForm(initial={ 'dates': CHOICES}, auto_id = auto_id_given, prefix = prefix_given)
    form_dates.fields['dates'].choices = CHOICES

    return form_dates


'''