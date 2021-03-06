# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_fanprofile_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fanprofile',
            name='title',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
    ]
