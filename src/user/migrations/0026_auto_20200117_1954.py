# Generated by Django 2.2.8 on 2020-01-17 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20200117_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='hub',
            new_name='hubs',
        ),
    ]