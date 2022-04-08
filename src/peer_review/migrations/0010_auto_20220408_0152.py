# Generated by Django 2.2 on 2022-04-08 01:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peer_review', '0009_auto_20220408_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peerreviewinvite',
            name='invited_by_user',
        ),
        migrations.RemoveField(
            model_name='peerreviewinvite',
            name='invited_email',
        ),
        migrations.RemoveField(
            model_name='peerreviewinvite',
            name='invited_user',
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 8, 1, 50, 37, 670209, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='inviter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='peerreviewinvite_sent_invites', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='key',
            field=models.CharField(default='', max_length=32, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peerreviewinvite_invitations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='peerreviewinvite',
            name='recipient_email',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
