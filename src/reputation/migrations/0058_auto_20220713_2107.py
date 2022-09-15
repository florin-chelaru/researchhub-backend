# Generated by Django 2.2 on 2022-07-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0057_delete_authorrsc'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='bounty',
            index=models.Index(fields=['item_content_type', 'item_object_id'], name='reputation__item_co_ad55e2_idx'),
        ),
        migrations.AddIndex(
            model_name='bounty',
            index=models.Index(fields=['solution_content_type', 'solution_object_id'], name='reputation__solutio_952e43_idx'),
        ),
        migrations.AddIndex(
            model_name='escrow',
            index=models.Index(fields=['content_type', 'object_id'], name='reputation__content_788513_idx'),
        ),
    ]