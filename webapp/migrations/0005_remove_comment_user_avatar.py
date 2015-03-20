# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_comment_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_avatar',
        ),
    ]
