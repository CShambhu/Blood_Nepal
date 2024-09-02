# Generated by Django 5.0.6 on 2024-08-30 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_banks', '0001_initial'),
        ('profile_', '0106_patient_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbanks',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profile_.signup'),
        ),
    ]