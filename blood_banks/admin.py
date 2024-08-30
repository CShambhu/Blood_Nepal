from django.contrib import admin

from blood_banks.models import BloodBanks

@admin.register(BloodBanks)
class BloodBanksAdmin(admin.ModelAdmin):
    list_display = ('id','blood_bank_name','blood_bank_location','blood_bank_phone','added_by_user')