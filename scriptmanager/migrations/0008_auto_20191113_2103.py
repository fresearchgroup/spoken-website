# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-13 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptmanager', '0007_auto_20190926_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
