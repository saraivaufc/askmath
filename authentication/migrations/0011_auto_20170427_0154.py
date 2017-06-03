# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=b'uploads/profile_image/%Y/%m/%d', verbose_name='Profile Image'),
        ),
    ]