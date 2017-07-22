# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 13:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0028_auto_20170721_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ask.Lesson', verbose_name='Lesson'),
            preserve_default=False,
        ),
    ]
