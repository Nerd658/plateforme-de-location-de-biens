# Generated by Django 5.0.6 on 2024-10-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="status",
            field=models.CharField(
                choices=[
                    ("en_attente", "En attente"),
                    ("paye", "Payé"),
                    ("annule", "Annulé"),
                ],
                default="en_attente",
                max_length=20,
            ),
        ),
    ]
