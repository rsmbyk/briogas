# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170811_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='katup',
            field=models.BooleanField(choices=[(True, 'Buka'), (False, 'Tutup')], default=False),
        ),
    ]
