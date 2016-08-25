import sys
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from main.models import Modules, UserProfile


def run():
    User = get_user_model()

    #  Update the users in this list.
    #  Each tuple represents the username, password, email, firstname and lastname of a user.
    users = [
        ('alexanderbouma', '123qweasdzxc', '-'),
        ('student', '123qweasdzxc', '-'),
        ('teacher', '123qweasdzxc', '-'),
    ]

    for username, password, email in users:
        try:
            print('Creating user: ', username)
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()

            assert authenticate(username=username, password=password)
            print('User ',username, ' successfully created.')

        except:
            print('There was a problem creating the user:', username, '. Error: ', sys.exc_info()[1])

    data_user = [   ['bramlap', 'Bram', 'Lap'],
                    ['alexanderbouma', 'Alexander', 'Bouma'],
                    ['student', 'Student', 'Student'],
                    ['teacher', 'Teacher', 'Teacher'],
    ]

    user_all = User.objects.all()
    userprofile_all = UserProfile.objects.all()


    for i in range(len(user_all)):
        does_exist = False
        for j in userprofile_all:
            if user_all[i] == j: 
                does_exist = True

        if does_exist == False :

            for j in range(len(data_user)):
                if str(user_all[i]) == str(data_user[j][0]):
                    if str(user_all[i]) == 'teacher':
                        p = UserProfile(
                            user        =   user_all[i],
                            firstname   =   str(data_user[j][1]), 
                            lastname    =   str(data_user[j][2]), 
                            is_student  =   False,
                            is_teacher  =   True,
                        )
                        p.save()
                    else:
                        p = UserProfile(
                            user        =   user_all[i],
                            firstname   =   str(data_user[j][1]), 
                            lastname    =   str(data_user[j][2]), 
                        )
                        p.save()

                    print('OK')


