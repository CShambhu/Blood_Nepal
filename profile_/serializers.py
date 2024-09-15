from rest_framework import serializers
from profile_.models import SignUp, Patient

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = '__all__'
        # fields = ('user','full_name','email','phone',
        #           'gender','profile_photo','location',
        #           'blood_group','weight','ready_to_donate','last_donation')
    
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ('user','blood_request_sent_by','blood_request_sent_to','message',
        #           'patients_name','hospital','patients_department','patients_gender',
        #           'patients_phone','patients_blood_group','blood_pint','required_date','created_at','requisition_form')










