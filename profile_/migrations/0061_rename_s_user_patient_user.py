# Generated by Django 5.0.6 on 2024-07-22 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0060_patient_s_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='S_user',
            new_name='user',
        ),
    ]
