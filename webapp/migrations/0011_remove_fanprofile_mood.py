# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20150321_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fanprofile',
            name='mood',
        ),
    ]
