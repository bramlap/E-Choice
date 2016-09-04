from django.contrib import admin
from main.models import UserProfile_General, UserProfile_Opleiding, Modules, User_Interesse_Opleidingen, Opleiding_module_data

# admin.site.register(UserProfile)
# admin.site.register(Questions)
admin.site.register(Modules)
admin.site.register(User_Interesse_Opleidingen)
admin.site.register(Opleiding_module_data)
admin.site.register(UserProfile_General)
admin.site.register(UserProfile_Opleiding)