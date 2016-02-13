# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160128_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='post',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
            preserve_default=False,
        ),
    ]
