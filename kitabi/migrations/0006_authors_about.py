# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitabi', '0005_book_summery'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='about',
            field=models.TextField(default=0, verbose_name='نبذة عن الكاتب'),
            preserve_default=False,
        ),
    ]
