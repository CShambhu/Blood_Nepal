# Generated by Django 5.0.6 on 2024-08-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0097_alter_patient_blood_request_sent_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='msg',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]