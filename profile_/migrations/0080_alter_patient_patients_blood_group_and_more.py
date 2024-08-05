# Generated by Django 5.0.6 on 2024-08-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0079_alter_signup_gender_alter_signup_ready_to_donate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patients_blood_group',
            field=models.CharField(choices=[('O+', 'O positive'), ('O-', 'O negative'), ('A+', 'A positive'), ('A-', 'A negative'), ('B+', 'B positive'), ('B-', 'B negative'), ('AB+', 'AB positive'), ('AB-', 'AB negative')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patients_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=6, null=True),
        ),
    ]
