# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-02-03 22:37
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaround_labels_comm', '0004_remove_player_chat_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='role',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]