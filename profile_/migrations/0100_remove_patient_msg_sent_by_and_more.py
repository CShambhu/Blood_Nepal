# Generated by Django 5.0.6 on 2024-08-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0099_remove_patient_msg_patient_msg_sent_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='msg_sent_by',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='msg_sent_to',
        ),
        migrations.AddField(
            model_name='patient',
            name='msg',
            field=models.TextField(max_length=50, null=True),
        ),
    ]