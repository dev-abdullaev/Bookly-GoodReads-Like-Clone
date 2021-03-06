# Generated by Django 4.0 on 2022-01-09 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_alter_favorite_is_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='is_added',
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorites',
            field=models.ManyToManyField(related_name='user_favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
