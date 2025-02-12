# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_comment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['date'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[(b'd', 'Draft'), (b'p', 'Published'), (b'r', 'Removed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('r', 'Removed')], max_length=1),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='status',
            field=models.CharField(choices=[(b'd', 'Draft'), (b'p', 'Published'), (b'r', 'Removed')], max_length=1),
        ),
    ]
