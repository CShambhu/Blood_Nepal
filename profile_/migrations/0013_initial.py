# Generated by Django 5.0.6 on 2024-06-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_', '0012_delete_sign_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=10)),
                ('first', models.CharField(max_length=120)),
                ('last', models.CharField(max_length=120)),
                ('phone', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]
