# Generated by Django 5.0.6 on 2024-08-12 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0082_rename_requestedby_patient_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='signup',
            new_name='requested_by',
        ),
    ]
