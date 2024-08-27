# Generated by Django 5.0.6 on 2024-08-27 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0103_patient_reply_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_message', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='reply_message',
        ),
    ]