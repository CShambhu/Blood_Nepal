# Generated by Django 5.0.6 on 2024-07-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0032_employee_rename_user_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.AddField(
            model_name='signup',
            name='user_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
