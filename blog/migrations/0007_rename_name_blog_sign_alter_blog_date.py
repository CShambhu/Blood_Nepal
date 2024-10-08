# Generated by Django 5.0.6 on 2024-07-21 08:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='sign',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
    ]
