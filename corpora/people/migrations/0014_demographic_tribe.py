# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_auto_20171113_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='demographic',
            name='tribe',
            field=models.ManyToManyField(to='people.Tribe'),
        ),
    ]