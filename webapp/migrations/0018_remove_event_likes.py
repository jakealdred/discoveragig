# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20150324_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='likes',
        ),
    ]
