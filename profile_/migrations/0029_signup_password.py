# Generated by Django 5.0.6 on 2024-07-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0028_remove_signup_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
