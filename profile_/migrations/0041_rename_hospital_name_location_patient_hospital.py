# Generated by Django 5.0.6 on 2024-07-12 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0040_rename_hospital_name_location_patient_hospital_name_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='hospital_name_location',
            new_name='hospital',
        ),
    ]
