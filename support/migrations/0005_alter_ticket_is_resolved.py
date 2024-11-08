# Generated by Django 5.0.7 on 2024-08-06 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("support", "0004_alter_ticket_is_resolved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="is_resolved",
            field=models.ForeignKey(
                blank=True,
                default=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resolved_ticket",
                to="support.ticketupdate",
            ),
        ),
    ]
