# Generated by Django 5.0.6 on 2024-06-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0020_alter_sign_up_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Sign_Up',
        ),
    ]
