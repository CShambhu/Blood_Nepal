# Generated by Django 5.0.6 on 2024-08-30 05:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_banks', '0002_bloodbanks_added_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodbanks',
            name='added_by',
        ),
        migrations.AddField(
            model_name='bloodbanks',
            name='added_by_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]