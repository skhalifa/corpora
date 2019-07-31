# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-24 05:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcription', '0023_auto_20190420_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofiletranscription',
            name='errors',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None, help_text='Place to store any error information.', null=True),
        ),
        migrations.AddField(
            model_name='audiofiletranscription',
            name='ignore',
            field=models.BooleanField(default=False, help_text='Help us find and ignore bad files/uploads.'),
        ),
    ]
