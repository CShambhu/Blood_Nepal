from .models import SignUp, Patient
from django import forms
from django.forms import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'

#Users SignUp Form
class SignUp_Form(forms.ModelForm):
    
    class Meta:
        model = SignUp
        fields = ('full_name','email','phone','gender','weight','profile_photo','location','blood_group','last_donation','ready_to_donate')
        # labels = {
        #     'full_name':'',
        #     'email':'',
        #     'phone':'',
        #     'gender':'',
        #     'weight':'',
        #     'profile_photo':'',
        #     'location':'',
        #     'blood_group':'',
        #     'last_donation':'',
        #     'ready_to_donate':'',
        # }
        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs= {'class':'form-control','placeholder':"example@gmail.com"}),
            'phone':forms.TextInput(attrs={"class":"form-control",'maxlength': '10'}),
            'gender':forms.RadioSelect(),
            'weight':forms.NumberInput(attrs={'class':'form-control'}),
            'profile_photo':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':"Your Photo"}),
            'location':forms.TextInput(attrs= {'class':'form-control','placeholder':"district,placename(kathmandu,baneshwor)"}),
            'blood_group':forms.Select(),
            'last_donation':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'ready_to_donate': forms.RadioSelect(),
            }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Make the full_name field read-only
    #     self.fields['full_name'].widget.attrs['readonly'] = True
        

        


#Patients SignUp Form
class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('full_name','hospital','patients_department','patients_gender','patients_phone','patients_blood_group','blood_pint','required_date','requisition_form')
    

        widgets = {
            'full_name':forms.TextInput(attrs={'class': 'form-control'}),
            'hospital':forms.TextInput(attrs= {'class':'form-control','placeholder':"Hospital name and location"}),
            'patients_department':forms.TextInput(attrs={'class':'form-control'}),
            'patients_gender':forms.RadioSelect(),
            'patients_phone':forms.NumberInput(attrs={"class":"form-control",'maxlength': '10'}),
            'patients_blood_group':forms.Select(),
            'blood_pint':forms.NumberInput(attrs={'class':'form-control'}),
            'required_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'requisition_form':forms.ClearableFileInput(attrs={'class':'form-control','placeholder':"Your Photo"}),

        }

