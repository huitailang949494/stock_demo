# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='module',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
