# Generated by Django 2.2 on 2021-06-04 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0009_researchhubpost_preview_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchhubpost',
            name='hubs',
        ),
    ]