from django.db import models

# Create your models here.
class BloodBanks(models.Model):
    blood_bank_name = models.CharField(max_length=100)
    blood_bank_location = models.CharField(max_length=50)
    blood_bank_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.blood_bank_name