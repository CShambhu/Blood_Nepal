# Generated by Django 5.0.6 on 2024-08-16 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0092_rename_blood_request_received_patient_blood_request_received_from_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='blood_request_received_from',
        ),
        migrations.AddField(
            model_name='patient',
            name='blood_request_sent_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_to', to='profile_.signup'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_request_sent_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_by', to='profile_.signup'),
        ),
    ]
