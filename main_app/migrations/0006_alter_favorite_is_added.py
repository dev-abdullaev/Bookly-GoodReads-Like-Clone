# Generated by Django 4.0 on 2022-01-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_favorite_is_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='is_added',
            field=models.TextField(default='not-added'),
        ),
    ]
