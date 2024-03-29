# Generated by Django 4.1.3 on 2023-02-18 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_wants_coat_styling_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='wants_obedience_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='wants_performance_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='services',
            name='wants_protection_training',
            field=models.BooleanField(default=False),
        ),
    ]
