# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_remove_achievement_xp'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='genre',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
