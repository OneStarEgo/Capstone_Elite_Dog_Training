# Generated by Django 4.1.3 on 2022-12-11 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_rename_user_pet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='breed',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
