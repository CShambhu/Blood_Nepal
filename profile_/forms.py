from .models import SignUp, Patient, Message
from django import forms
from django.forms import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'

#Users SignUp Form
class SignUp_Form(forms.ModelForm):
    
    class Meta:
        model = SignUp
        fields = ('full_name','email','phone','gender','weight','profile_photo','location','blood_group','last_donation','ready_to_donate')
        
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs= {'class':'form-control','placeholder':"example@gmail.com"}),
            'phone':forms.TextInput(attrs={"class":"form-control",'maxlength': '10'}),
            'gender':forms.Select(),
            'weight':forms.NumberInput(attrs={'class':'form-control'}),
            'profile_photo':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs= {'class':'form-control','placeholder':"district,placename"}),
            'blood_group':forms.Select(),
            'last_donation':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'ready_to_donate': forms.Select(),
            }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Make the full_name field read-only
    #     self.fields['full_name'].widget.attrs['readonly'] = True

    
#Patients SignUp Form
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patients_name','hospital','patients_department','patients_gender','patients_phone','patients_blood_group','blood_pint','required_date','requisition_form','message')
        widgets = {
            'patients_name':forms.TextInput(attrs={'class': 'form-control'}),
            'hospital':forms.TextInput(attrs= {'class':'form-control','placeholder':"Hospital name and location"}),
            'patients_department':forms.TextInput(attrs={'class':'form-control'}),
            'patients_gender':forms.Select(),
            'patients_phone':forms.TextInput(attrs={"class":"form-control"}),
            'patients_blood_group':forms.Select(),
            'blood_pint':forms.NumberInput(attrs={'class':'form-control'}),
            'required_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'requisition_form':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':"Your Photo"}),
            'message':forms.TextInput(attrs={'class':'form-control','placeholder':"Message to donor. e.g It's urgent | please be available on time | donor required on standby. "}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('id','reply_message')
        widgets = {
            'reply_message':forms.TextInput(attrs={'class':'form-control','placeholder':""}),
        }
