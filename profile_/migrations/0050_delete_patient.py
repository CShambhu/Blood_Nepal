# Generated by Django 5.0.6 on 2024-07-18 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0049_remove_patient_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
