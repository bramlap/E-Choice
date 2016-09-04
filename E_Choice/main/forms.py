from django import forms
from .models import Modules, UserProfile_General, UserProfile_Opleiding #UserProfile, Questions, 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

import time, datetime

'''
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname',  'weging_stud', 'weging_toek', 'weging_soc') #'questions'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class ModuleForm(forms.ModelForm):
	save_module = forms.IntegerField(initial=0)
	class Meta:
		model = Modules
		fields = ('cijfer',)

class ModulesDatesForm(forms.Form):
    dates = forms.ChoiceField()
    # dates = forms.CharField(max_length=35, choices=DATES, default='1 november 2016')
'''
class ModuleForm(forms.ModelForm):
    save_module = forms.IntegerField(initial=0)
    class Meta:
        model = Modules
        fields = ('cijfer',)

class SelecteerStudentForm(forms.ModelForm):
    class Meta:
        model = UserProfile_General
        fields = ('firstname', 'lastname',)

class SelecteerOpleidingForm(forms.ModelForm):
    class Meta:
        model = UserProfile_General
        fields = ('opleiding_selected', )

class BuyModuleForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields = ('buy_module', )

class UserOpleidingKiezenForm(forms.Form):
    wiskunde = forms.BooleanField()
    natuurkunde = forms.BooleanField()
    sterrenkunde = forms.BooleanField()
    scheikunde = forms.BooleanField()
    biologie = forms.BooleanField()
    lst = forms.BooleanField()
    farmacie = forms.BooleanField()
    informatica = forms.BooleanField()
    ki = forms.BooleanField()
    tbk = forms.BooleanField()

    helper = FormHelper()
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    # helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('wiskunde', style="background: #FAFAFA; padding: 10px; left:-10px; bottom:0.5%"),
        Field('natuurkunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('sterrenkunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('scheikunde', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('biologie', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('lst', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('farmacie', style="background: #FAFAFA; padding: 10px; left:-10px"),
        Field('informatica', style="background: #FAFAFA; padding: 10px; left:-10px"),
        FormActions(
            Submit('save_changes', 'Save', css_class="btn-primary"),
        )
    )

class UserProfileGeneralForm(forms.ModelForm):
    class Meta:
        model = UserProfile_General
        fields = ('firstname', 'lastname') #'questions'

class UserProfileOpleidingForm(forms.ModelForm):
    class Meta:
        model = UserProfile_Opleiding
        fields = ('weging_stud', 'weging_toek', 'weging_soc')

class ExportPDFForm(forms.Form):
	export_pdf = forms.IntegerField(initial=0)