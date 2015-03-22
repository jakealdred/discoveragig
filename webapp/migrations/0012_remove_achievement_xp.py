# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_remove_fanprofile_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='xp',
        ),
    ]
