# Generated by Django 5.1.6 on 2025-03-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("xvoice", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="sentiment",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
