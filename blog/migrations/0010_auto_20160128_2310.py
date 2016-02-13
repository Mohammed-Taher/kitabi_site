# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160128_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
    ]
