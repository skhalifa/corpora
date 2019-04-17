# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcription', '0021_audiofiletranscription_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcription',
            name='word_error_rate',
            field=models.FloatField(blank=True, default=None, editable=False, null=True),
        ),
    ]