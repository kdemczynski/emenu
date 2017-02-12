# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'karta menu',
                'verbose_name_plural': 'karty menu',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CardItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='restaurant.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prep_time', models.IntegerField()),
                ('vege', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'danie',
                'verbose_name_plural': 'dania',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='carditems',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to='restaurant.Dish'),
        ),
        migrations.AlterIndexTogether(
            name='card',
            index_together=set([('id', 'name')]),
        ),
    ]