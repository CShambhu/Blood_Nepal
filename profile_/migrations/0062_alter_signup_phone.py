# Generated by Django 5.0.6 on 2024-07-29 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0061_rename_s_user_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
