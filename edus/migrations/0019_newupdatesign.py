# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edus', '0018_auto_20170718_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUpdateSign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_signal', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('signal_id', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
