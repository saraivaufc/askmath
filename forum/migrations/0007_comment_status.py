# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20170204_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Removed')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
