# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160128_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='c_accept',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='c_website',
            field=models.URLField(),
        ),
    ]
