from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Users SignUp Form
class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 120, null=False, blank=False )
    email = models.EmailField( null=False, blank=False)
    phone=models.IntegerField()
    gender = models.CharField(max_length=1)
    profile_photo = models.ImageField(upload_to = 'images/')
    location = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=2)
    weight = models.IntegerField( null=True, blank=False)

    def __str__(self):
        return self.full_name

#Patients SignUp Form
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null= True)
    signup = models.ForeignKey(SignUp, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length = 20)
    hospital = models.CharField(max_length = 20, null=True)
    patients_department = models.CharField(max_length = 120)
    patients_phone = models.IntegerField(null=True,blank=True)
    blood_pint = models.IntegerField(null=True)
    patients_blood_group = models.CharField(max_length=10,null= True)
    requisition_form = models.ImageField(upload_to = 'patientsForm/')
    
    def __str__(self):
        return self.full_name