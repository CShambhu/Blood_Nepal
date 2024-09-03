from django.contrib import admin

from .models import SignUp, Patient, Message
# Register your models here.
@admin.register(SignUp)
class signupAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","user","email","location","blood_group")
    search_fields = ("id","full_name","user__username","email","location","blood_group")
    list_filter = ("location","blood_group")
    ordering = ["-id"]



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id","blood_request_sent_by","blood_request_sent_to","message","patients_name","hospital","patients_blood_group","required_date")
    search_fields = ("id","blood_request_sent_by__full_name","blood_request_sent_to__full_name","message","patients_name","hospital","patients_blood_group","required_date")




@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','reply_message')


