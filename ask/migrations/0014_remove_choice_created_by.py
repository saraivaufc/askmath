# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 02:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0013_auto_20170210_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='created_by',
        ),
    ]
