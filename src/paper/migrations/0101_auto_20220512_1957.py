# Generated by Django 2.2 on 2022-05-12 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0100_auto_20220512_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='score',
            new_name='paper_score',
        ),
        migrations.AlterField(
            model_name='flag',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags_legacy', related_query_name='flag_legacy', to='paper.Paper'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_legacy', related_query_name='vote_legacy', to='paper.Paper'),
        ),
    ]