# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrza', '0006_auto_20160318_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woche',
            name='mo_extra',
            field=models.PositiveSmallIntegerField(default=0, null=True),
        ),
    ]