# Generated by Django 5.0.6 on 2024-07-18 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0050_delete_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('hospital', models.CharField(max_length=20, null=True)),
                ('patients_department', models.CharField(max_length=120)),
                ('patients_phone', models.IntegerField(blank=True, null=True)),
                ('blood_pint', models.IntegerField(null=True)),
                ('patients_blood_group', models.CharField(max_length=10, null=True)),
                ('requisition_form', models.ImageField(upload_to='patientsForm/')),
                ('signup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_.signup')),
            ],
        ),
    ]
