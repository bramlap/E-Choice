from django import forms
from .models import UserProfile, Questions, Modules


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
        fields = ('buy_module',)

class ExportPDFForm(forms.Form):
	export_pdf = forms.IntegerField(initial=0)

class CounterRedirect(forms.Form):
    counter_redirect = forms.IntegerField(initial=0)
