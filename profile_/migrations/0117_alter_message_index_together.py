# Generated by Django 5.0.6 on 2024-09-05 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0116_alter_patient_blood_request_sent_by_and_more'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='message',
            index_together={('reply_message', 'message_sent_by', 'message_sent_to')},
        ),
    ]
