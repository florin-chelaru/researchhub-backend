# Generated by Django 4.1 on 2023-02-27 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reputation", "0069_remove_bounty_effort_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="escrow",
            name="status",
            field=models.CharField(
                choices=[
                    ("PAID", "PAID"),
                    ("PARTIALLY_PAID", "PARTIALLY_PAID"),
                    ("PENDING", "PENDING"),
                    ("CANCELLED", "CANCELLED"),
                ],
                default="PENDING",
                max_length=16,
            ),
        ),
    ]
