# Generated by Django 5.0.6 on 2024-07-22 15:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
