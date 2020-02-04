# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-02-04 19:28
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('turnaround_labels_pun', '0002_auto_20200204_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='long_reflection',
        ),
        migrations.RemoveField(
            model_name='player',
            name='role',
        ),
        migrations.AddField(
            model_name='player',
            name='vote',
            field=otree.db.models.StringField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10000, null=True, verbose_name=''),
        ),
    ]
