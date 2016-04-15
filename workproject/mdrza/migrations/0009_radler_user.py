# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mdrza', '0008_auto_20160318_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='radler',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]