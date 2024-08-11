from django.contrib import admin

from .models import SignUp, Patient
# Register your models here.

class signupAdmin(admin.ModelAdmin):
    list_display = ["full_name","user","email","location","blood_group"]

class PatientAdmin(admin.ModelAdmin):
    list_display = ["full_name","hospital","patients_blood_group","required_date"]


admin.site.register(SignUp,signupAdmin)
admin.site.register(Patient,PatientAdmin)



