# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0026_auto_20170314_0726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='color',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='color',
        ),
        migrations.RemoveField(
            model_name='video',
            name='color',
        ),
    ]
