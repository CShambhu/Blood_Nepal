# Generated by Django 5.0.6 on 2024-07-09 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0035_remove_login_user_name_login_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='user_name',
        ),
    ]
