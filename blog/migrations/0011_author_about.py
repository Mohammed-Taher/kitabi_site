# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-29 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160128_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]