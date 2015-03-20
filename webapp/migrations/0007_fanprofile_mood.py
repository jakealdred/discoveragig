# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20150320_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanprofile',
            name='mood',
            field=models.TextField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
