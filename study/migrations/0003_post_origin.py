# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-26 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20170326_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='origin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='원본 URL'),
        ),
    ]