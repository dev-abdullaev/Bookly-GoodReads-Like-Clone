# Generated by Django 3.2.7 on 2022-01-10 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
