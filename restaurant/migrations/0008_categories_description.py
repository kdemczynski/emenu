# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
