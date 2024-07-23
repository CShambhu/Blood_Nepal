# Generated by Django 5.0.6 on 2024-07-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0034_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='user_name',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
