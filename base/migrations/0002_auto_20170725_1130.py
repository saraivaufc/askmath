# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialnetwork',
            name='created_by',
        ),
        migrations.AddField(
            model_name='emailmarketing',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
