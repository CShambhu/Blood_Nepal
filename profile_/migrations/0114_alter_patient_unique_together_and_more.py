# Generated by Django 5.0.6 on 2024-09-05 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0113_delete_patientcopy'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together={('patients_phone',)},
        ),
        migrations.AlterUniqueTogether(
            name='signup',
            unique_together={('email', 'phone')},
        ),
    ]