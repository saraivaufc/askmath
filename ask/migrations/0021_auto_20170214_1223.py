# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0020_auto_20170214_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
