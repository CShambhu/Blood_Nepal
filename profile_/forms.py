from .models import SignUp
from django import forms
from django.forms import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'

#Users SignUp Form
class SignUp_Form(forms.Form):
    GenderChoices = [
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    ]

    Blood_Group_Choices = [
        ('O+', 'O positive'),
        ('O-', 'O negative'),
        ('A+', 'A positive'),
        ('A-', 'A negative'),
        ('B+', 'B positive'),
        ('B-', 'B negative'),
        ('AB+', 'AB positive'),
        ('AB-', 'AB negative'),
    ]
    R_CHOICES = [
        ('yes', 'Yes'),   ('no', 'No')   
    ]

    #name
    full_name = forms.CharField(
        max_length = 120,
        widget = forms.TextInput(attrs={
            'class': 'form-control'
        })
        )
    
    #email
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'class':'form-control',
                'placeholder':"example@gmail.com"
            })
        )
    
    #phone
    phone = forms.CharField(
        widget=forms.TextInput(
             attrs={
                 "class":"form-control",
                 'maxlength': '10'
             }
        )
    )


    
    #gender
    gender = forms.ChoiceField(
        choices=GenderChoices,
        widget=forms.RadioSelect
        )
    
    # Weight
    weight = forms.IntegerField()

    
    #image
    profile_photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
            'class':'form-control',
            'placeholder':"Your Photo"
            })
        )
    
    #location
    location = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':"district,placename(kathmandu,baneshwor)"
            })
        )
    
    #blood
    blood_group = forms.CharField(
        widget=forms.Select(choices=Blood_Group_Choices),
        max_length=3
        )

    #last donation date
    last_donation = forms.DateField(widget=DateInput)
    
    #donar is ready to donate
    ready_to_donate = forms.ChoiceField(
        choices=R_CHOICES,
        widget= forms.RadioSelect
    )

    

    



#Patients SignUp Form
class PatientsForm(forms.Form):
    #Full_name
    full_name = forms.CharField(
                widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'placeholder':"patient's full name"
            }
        )
    )

    #Hospital's name and Location
    hospital = forms.CharField(
        widget=forms.TextInput(
            attrs= {
                'class':'form-control',
                'placeholder':"Hospital's name, location"
            })
        )
    
    #Patient's Department
    patients_department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'placeholder':"patient's admitted department"
            }
        )
    )

    #Patients Phone
    patients_phone = forms.CharField(
            widget=forms.TextInput(
             attrs={
                 "class":"form-control",
                 'maxlength': '10'
             }
        )
    )

    #Required Blood Group
    patients_blood_group = forms.CharField(
        widget=forms.Select(choices = SignUp_Form.Blood_Group_Choices),
        max_length=3
        )
    
    #Amount of Blood Required
    blood_pint = forms.CharField(
                widget=forms.TextInput(
            attrs={
                "class":"form-control",
                'placeholder':"amount of blood required",
                'max_length':'3'
            }
        )
    )

    #Blood Requisition Form
    requisition_form = forms.ImageField(
        widget= forms.ClearableFileInput(
            attrs=(
            {'class':'form-control',
            'placeholder':"requisition form provided by hospital"
            })
        )
    )

