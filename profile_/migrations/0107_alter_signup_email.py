# Generated by Django 5.0.6 on 2024-09-05 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0106_patient_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]