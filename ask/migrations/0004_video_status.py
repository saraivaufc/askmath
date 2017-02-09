# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.CharField(choices=[(b'd', 'Draft'), (b'p', 'Published'), (b'r', 'Removed')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
