# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0003_remove_acceptlicense_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='license_display',
            field=models.TextField(help_text='How the license should be displayed. This field is meant                    to include style e.g. html.', null=True),
        ),
    ]