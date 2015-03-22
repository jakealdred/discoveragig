# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_auto_20150322_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
