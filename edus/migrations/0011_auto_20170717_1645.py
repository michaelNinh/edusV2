# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edus', '0010_auto_20170717_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useredus',
            name='votes',
        ),
        migrations.AddField(
            model_name='question',
            name='voters',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voters', to='edus.UserEdus'),
        ),
    ]
