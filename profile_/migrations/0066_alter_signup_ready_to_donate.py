# Generated by Django 5.0.6 on 2024-08-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0065_alter_signup_ready_to_donate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='ready_to_donate',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=4, null=True),
        ),
    ]
