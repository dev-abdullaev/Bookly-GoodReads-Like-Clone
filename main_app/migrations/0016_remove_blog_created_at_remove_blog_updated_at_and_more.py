# Generated by Django 4.0 on 2022-01-10 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_rename_added_date_favorite_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='updated_at',
        ),
    ]
