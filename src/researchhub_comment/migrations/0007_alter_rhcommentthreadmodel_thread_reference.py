# Generated by Django 4.1 on 2023-01-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("researchhub_comment", "0006_rhcommentmodel_legacy_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rhcommentthreadmodel",
            name="thread_reference",
            field=models.CharField(
                blank=True,
                help_text="A thread may need a special referencing tool. Use this field for such a case",
                max_length=144,
                null=True,
            ),
        ),
    ]