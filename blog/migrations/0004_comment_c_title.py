# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160128_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='c_title',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
