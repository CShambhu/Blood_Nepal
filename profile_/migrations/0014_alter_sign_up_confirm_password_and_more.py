# Generated by Django 5.0.6 on 2024-06-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0013_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sign_up',
            name='confirm_password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
