# Generated by Django 5.0.6 on 2024-08-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0093_remove_patient_blood_request_received_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='required_date',
            field=models.DateTimeField(null=True),
        ),
    ]
