from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    user = models.OneToOneField(User, on_delete = models.CASCADE , unique=True)
    full_name = models.CharField(max_length = 120, null=False, blank=False )
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10,null=True)
    gender = models.CharField(max_length=6, choices= GenderChoices , default='Male')
    profile_photo = models.ImageField(upload_to = 'images/')
    location = models.CharField(max_length=40)
    blood_group = models.CharField(choices=Blood_Group_Choices,max_length=3)
    weight = models.IntegerField( null=True, blank=False)
    ready_to_donate = models.CharField(choices=R_CHOICES ,null=True, max_length=4)
    last_donation = models.DateField(null=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        unique_together = ('email','phone')


#Patients SignUp Form
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null= True)
    blood_request_sent_by = models.ForeignKey(SignUp,related_name='sent_by',verbose_name = "sender" , on_delete=models.PROTECT, null=True, blank=True)
    blood_request_sent_to = models.ForeignKey(SignUp,related_name='sent_to',verbose_name= "receiver",  on_delete=models.PROTECT, null=True, blank=False)
    message = models.TextField(max_length = 50, null=True)
    patients_name = models.CharField(max_length = 20)
    hospital = models.CharField(max_length = 20, null=True)
    patients_department = models.CharField(max_length = 120)
    patients_gender = models.CharField(max_length=6, choices= GenderChoices, null=True, default='Male')
    patients_phone = models.CharField(max_length=10, null=True,blank=True)
    patients_blood_group = models.CharField(choices=Blood_Group_Choices,max_length=3,null= True)
    blood_pint = models.IntegerField(null=True)
    required_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    requisition_form = models.ImageField(upload_to = 'patientsForm/')

    def __str__(self):
        return self.patients_name
    
    
    

    
    # class Meta:
    #     unique_together = ('patients_phone',)
    #     ordering  = ['user','patients_name','hospital','patients_department',
    #                  'patients_gender','patients_phone','patients_blood_group',
    #                  'blood_pint','required_date','created_at','requisition_form','blood_request_sent_by','blood_request_sent_to']
    


class Message(models.Model):
    reply_message = models.TextField(max_length = 50, null=True)
    message_sent_by = models.ForeignKey(SignUp,related_name='message_sent_by', on_delete=models.SET_NULL, null=True, blank=True)
    message_sent_to = models.ForeignKey(SignUp,related_name='message_sent_to', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.reply_message 
    
    # class Meta:
    #     index_together = ('reply_message', 'message_sent_by')
    