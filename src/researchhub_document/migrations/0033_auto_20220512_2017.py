# Generated by Django 2.2 on 2022-05-12 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('researchhub_document', '0032_feedexclusion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedexclusion',
            name='unified_document',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='excluded_from_feeds', to='researchhub_document.ResearchhubUnifiedDocument'),
        ),
    ]