# Generated by Django 5.1.5 on 2025-01-31 00:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_etudiant_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='valeur',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
