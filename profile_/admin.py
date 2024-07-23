from django.contrib import admin

from .models import SignUp, Patient
# Register your models here.
admin.site.register(SignUp)
admin.site.register(Patient)

class signupAdmin(admin.ModelAdmin):
    list_display = ["id","full_name","email","location","blood_group"]
