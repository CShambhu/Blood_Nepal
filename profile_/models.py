from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Users SignUp Form
R_CHOICES = [
        ('yes', 'Yes'),  
        ('no', 'No')   
    ]

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

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 120, null=False, blank=False )
    email = models.EmailField( null=False, blank=False)
    phone = models.IntegerField(null=True)
    gender = models.CharField(max_length=6, choices= GenderChoices , default='Male')
    profile_photo = models.ImageField(upload_to = 'images/')
    location = models.CharField(max_length=40)
    blood_group = models.CharField(choices=Blood_Group_Choices,max_length=3)
    weight = models.IntegerField( null=True, blank=False)
    ready_to_donate = models.CharField(choices=R_CHOICES ,null=True, max_length=4)
    last_donation = models.DateField(null=True)
    
    def __str__(self):
        return self.full_name

#Patients SignUp Form
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null= True)
    blood_requested_by = models.ForeignKey(SignUp,related_name='requested', on_delete=models.SET_NULL, null=True, blank=True)
    blood_requested_to = models.ForeignKey(SignUp,related_name='sent', on_delete=models.SET_NULL, null=True, blank=False)
    patients_name = models.CharField(max_length = 20)
    hospital = models.CharField(max_length = 20, null=True)
    patients_department = models.CharField(max_length = 120)
    patients_gender = models.CharField(max_length=6, choices= GenderChoices, null=True, default='Male')
    patients_phone = models.IntegerField( null=True,blank=True)
    patients_blood_group = models.CharField(choices=Blood_Group_Choices,max_length=3,null= True)
    blood_pint = models.IntegerField(null=True)
    required_date = models.DateField(null=True)
    requisition_form = models.ImageField(upload_to = 'patientsForm/')
    
    def __str__(self):
        return self.patients_name
    