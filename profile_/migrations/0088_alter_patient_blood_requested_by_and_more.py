# Generated by Django 5.0.6 on 2024-08-12 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0087_alter_patient_blood_requested_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_requested_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested', to='profile_.signup'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_requested_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent', to='profile_.signup'),
        ),
    ]
