# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practices', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeworkitemtimer',
            old_name='practice_session',
            new_name='practice',
        ),
        migrations.RemoveField(
            model_name='practice',
            name='homework_item_timers',
        ),
    ]
