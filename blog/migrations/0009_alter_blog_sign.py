# Generated by Django 5.0.6 on 2024-07-22 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_author'),
        ('profile_', '0059_alter_signup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='sign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sign', to='profile_.signup'),
        ),
    ]
