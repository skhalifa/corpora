# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-12 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20171112_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='license',
            new_name='license_name',
        ),
    ]
