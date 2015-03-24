# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bandprofile',
            name='mood',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='views',
        ),
        migrations.RemoveField(
            model_name='event',
            name='price',
        ),
    ]
