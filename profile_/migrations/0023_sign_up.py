# Generated by Django 5.0.6 on 2024-06-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_', '0022_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20, null=True)),
                ('first', models.CharField(max_length=120)),
                ('last', models.CharField(max_length=120)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(max_length=50)),
            ],
        ),
    ]
