# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_formats', '0002_auto_20161109_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logformats',
            name='log_format',
            field=models.CharField(max_length=100),
        ),
    ]
