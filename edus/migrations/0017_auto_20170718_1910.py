# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edus', '0016_question_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='document',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to='MEDIA_ROOT/documents/'),
        ),
    ]