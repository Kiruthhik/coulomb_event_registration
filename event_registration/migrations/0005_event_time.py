# Generated by Django 5.0.1 on 2025-02-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration', '0004_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
