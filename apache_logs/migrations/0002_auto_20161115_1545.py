# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apache_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apachelog',
            name='time_received_tz_isoformat',
            field=models.DateTimeField(max_length=50, null=True),
        ),
    ]
