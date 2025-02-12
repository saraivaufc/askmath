# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20170214_1159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['creation'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-last_modified'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Text'),
        ),
    ]
