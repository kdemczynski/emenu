# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20170211_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='sort',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]