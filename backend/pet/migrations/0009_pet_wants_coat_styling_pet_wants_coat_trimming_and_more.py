# Generated by Django 4.1.3 on 2023-02-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0008_alter_pet_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='wants_coat_styling',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='wants_coat_trimming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='wants_obedience_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='wants_performance_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pet',
            name='wants_protection_training',
            field=models.BooleanField(default=False),
        ),
    ]