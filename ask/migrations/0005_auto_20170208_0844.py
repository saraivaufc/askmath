# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_video_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
