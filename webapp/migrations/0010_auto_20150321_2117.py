# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(max_length=16),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fanprofile',
            name='title',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
