from django.contrib import admin

from .models import SignUp, Patient, Message
# Register your models here.
@admin.register(SignUp)
class signupAdmin(admin.ModelAdmin):
    list_display = ["id","full_name","user","email","location","blood_group"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["id","blood_request_sent_by","blood_request_sent_to","message","patients_name","hospital","patients_blood_group","required_date"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','reply_message']


