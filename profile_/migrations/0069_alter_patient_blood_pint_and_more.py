# Generated by Django 5.0.6 on 2024-08-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0068_alter_patient_blood_pint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_pint',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patients_phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
