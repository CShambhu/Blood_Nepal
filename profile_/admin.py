from django.contrib import admin

from .models import SignUp, Patient
# Register your models here.
@admin.register(SignUp)
class signupAdmin(admin.ModelAdmin):
    list_display = ["id","full_name","user","email","location","blood_group"]
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["id","blood_request_sent_by","blood_request_sent_to","patients_name","hospital","patients_blood_group","required_date"]


# admin.site.register(SignUp,signupAdmin)
# admin.site.register(Patient,PatientAdmin)



