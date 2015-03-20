# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20150318_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_avatar',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
