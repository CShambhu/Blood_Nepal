# Generated by Django 5.0.6 on 2024-08-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0102_alter_patient_patients_phone_alter_signup_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='reply_message',
            field=models.TextField(max_length=50, null=True),
        ),
    ]