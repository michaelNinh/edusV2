# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edus', '0002_auto_20170716_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voters',
            field=models.ManyToManyField(null=True, related_name='voters', to='edus.UserEdus'),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reply',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
