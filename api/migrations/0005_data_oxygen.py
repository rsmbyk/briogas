# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170811_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='oxygen',
            field=models.IntegerField(default=0),
        ),
    ]
