# Generated by Django 2.2 on 2022-03-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reputation', '0045_withdrawal_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawal',
            name='token_address',
            field=models.CharField(choices=[('', 'ResearchCoin address')], max_length=255),
        ),
    ]