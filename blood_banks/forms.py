from django import forms
from blood_banks.models import BloodBanks
class BloodBanksForm(forms.ModelForm):
    class Meta:
        model = BloodBanks
        fields = ('blood_bank_name','blood_bank_location','blood_bank_phone')
        widgets = {
            'blood_bank_name':forms.TextInput(attrs={'class':'form-control'}),
            'blood_bank_location':forms.TextInput(attrs={'class':'form-control'}),
            'blood_bank_phone':forms.TextInput(attrs={'class':'form-control'}),
        }