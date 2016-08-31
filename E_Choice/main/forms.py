from django import forms
from .models import UserProfile, Questions, Modules
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

import time, datetime

# nov_01_16_remove = False
DATES = (
    ('1 november 2016', '1 november 2016'),
    ('1 februari 2016', '1 februari 2016'),
    ('1 april 2016', '1 april 2016')
)

DATES_1 = (
    ('1 november 2016', str(datetime.datetime.now()) ),
    ('1 februari 2016', '1 februari 2016'),
    ('1 april 2016', '1 april 2016')
)

CHOICES = []

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

class BuyModuleForm(forms.ModelForm):
    class Meta:
        model = Modules
        fields = ('buy_module', )

class ModulesDatesForm(forms.Form):
    dates = forms.ChoiceField()
    # dates = forms.CharField(max_length=35, choices=DATES, default='1 november 2016')

class OpleidingKiezenForm(forms.Form):
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


    '''  
def __init__(self, *args, **kwargs):
            super(BuyModuleForm, self).__init__(*args, **kwargs)

            import time, datetime
            #datetime.datetime( year, month, day, hour, minute, second), year/month/day are required
            localtime = time.localtime(time.time())
            # year = localtime[0]
            # month = localtime[1]
            # day = localtime[2]
            # hour = localtime[3]+2
            # minute = localtime[4] 
            second = localtime[5]
            nov_01_16 = datetime.datetime(2016, 7, 1, 0, 0, 0)
            feb_01_17 = datetime.datetime(2017, 2, 1, 0, 0, 0)
            apr_01_17 = datetime.datetime(2017, 4, 1, 0, 0, 0)
            now = datetime.datetime.now()
            # tijdje = datetime.datetime(2016, 8, 29, 0, 0, 0)

            # names = list(self.fields['id_module'])

            # print("id_module", names)

            # print("joden")
            # if nov_01_16_remove == False:
            if second > 30 :
                new_choices = list(self.fields['date'].choices)
                # print("new_choices: ", new_choices)
                # print("self: ", self)

                for i in self:
                    print(i['id'])

                new_choices.remove(('1 november 2016', '1 november 2016'))
                self.fields['date'].choices = new_choices
                self.fields['date'].widget.choices = new_choices
                nov_01_16_remove = True

            #             if nov_01_16_remove == False:
            #     if now > nov_01_16 :
            #         new_choices = list(self.fields['date'].choices)
            #         new_choices.remove(('1 november 2016', '1 november 2016'))
            #         self.fields['date'].choices = new_choices
            #         self.fields['date'].widget.choices = new_choices
            #         nov_01_16_remove = True

            # if feb_01_17_remove == False:               
            #     if now > feb_01_17 :
            #         new_choices = list(self.fields['date'].choices)
            #         new_choices.remove(('1 feb 2016', '1 feb 2016'))
            #         self.fields['date'].choices = new_choices
            #         self.fields['date'].widget.choices = new_choices
            #         nov_01_16_remove = True
                        
            # if apr_01_17_remove == False:               
            #     if now > nov_01_16 :
            #         new_choices = list(self.fields['date'].choices)
            #         new_choices.remove(('1 november 2016', '1 november 2016'))
            #         self.fields['date'].choices = new_choices
            #         self.fields['date'].widget.choices = new_choices
                    # nov_01_16_remove = True


    '''

class ExportPDFForm(forms.Form):
	export_pdf = forms.IntegerField(initial=0)