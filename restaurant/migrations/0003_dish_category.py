# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20170210_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('WEGE', 'Dania wegetariańskie'), ('MIESO', 'Dania mięsne'), ('MAKA', 'Dania mączne'), ('ZUPA', 'Zupy'), ('NAPOJ', 'Napoje'), ('ALKOHOL', 'Alkohole'), ('DESER', 'Desery'), ('INNE', 'Inne')], default='INNE', max_length=2),
        ),
    ]
