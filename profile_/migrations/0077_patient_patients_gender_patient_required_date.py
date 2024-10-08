# Generated by Django 5.0.6 on 2024-08-05 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0076_alter_signup_blood_group_alter_signup_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patients_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='required_date',
            field=models.DateField(null=True),
        ),
    ]
