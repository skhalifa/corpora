# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0002_acceptlicense_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptlicense',
            name='accepted',
        ),
    ]
