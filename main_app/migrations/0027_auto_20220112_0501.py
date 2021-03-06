# Generated by Django 3.2.7 on 2022-01-12 05:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20220112_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='stars_given',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='bookreview',
            name='stars_given',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
