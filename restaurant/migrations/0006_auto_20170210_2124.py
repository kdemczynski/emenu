# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20170210_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('MIESO', 'Dania mięsne'), ('MAKA', 'Dania mączne'), ('ZUPA', 'Zupy'), ('NAPOJ', 'Napoje'), ('ALKOHOL', 'Alkohole'), ('DESER', 'Desery'), ('INNE', 'Inne')], default='INNE', max_length=50),
        ),
    ]
