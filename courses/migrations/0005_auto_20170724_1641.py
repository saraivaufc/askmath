# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170724_1631'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='learningobject',
            unique_together=set([]),
        ),
    ]
