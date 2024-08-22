# Generated by Django 5.0.6 on 2024-08-17 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0096_alter_patient_blood_request_sent_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_request_sent_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_by', to='profile_.signup'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_request_sent_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_to', to='profile_.signup'),
        ),
    ]