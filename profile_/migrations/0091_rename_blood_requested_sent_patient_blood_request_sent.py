# Generated by Django 5.0.6 on 2024-08-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0090_remove_patient_blood_requested_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='blood_requested_sent',
            new_name='blood_request_sent',
        ),
    ]