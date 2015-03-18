# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20150318_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
