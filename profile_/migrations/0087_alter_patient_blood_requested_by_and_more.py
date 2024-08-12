# Generated by Django 5.0.6 on 2024-08-12 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0086_rename_full_name_patient_patients_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_by', to='profile_.signup'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_requested_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_to', to='profile_.signup'),
        ),
    ]