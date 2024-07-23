from .models import SignUp
from django import forms
from django.forms import ValidationError


#Users SignUp Form
class SignUp_Form(forms.Form):
    GenderChoices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
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
    phone=forms.IntegerField()
    
    #gender
    gender = forms.CharField(
        widget=forms.Select(choices=GenderChoices),
        max_length=6
        )
    
    # Weight
    weight = forms.IntegerField(
        widget= forms.NumberInput(
            attrs=(
            {'class':'form-control',

            })
        )
    )
    
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

    # def clean(self):
    #     if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    #         raise forms.ValidationError("The password does not match ")
    #     return self.cleaned_data



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
    patients_phone = forms.IntegerField(
        #         widget=forms.TextInput(
        #     attrs={
        #         "class":"form-control",
        #         'placeholder':"patient's caretaker at hospital "
        #     }
        # )
    )

    #Required Blood Group
    patients_blood_group = forms.CharField(
        widget=forms.Select(choices = SignUp_Form.Blood_Group_Choices),
        max_length=3
        )
    
    #Amount of Blood Required
    blood_pint = forms.IntegerField(
                widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                'placeholder':"amount of blood required"
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

