# Generated by Django 5.0.6 on 2024-07-22 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_name_blog_sign_alter_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
