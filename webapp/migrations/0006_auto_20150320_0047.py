# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_remove_comment_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=2, choices=[(b'GL', b'Glasgow'), (b'ED', b'Edinburgh'), (b'AB', b'Aberdeen'), (b'LO', b'London'), (b'DU', b'Dundee')])),
                ('genre', models.CharField(max_length=16, choices=[(b'rock', b'Rock'), (b'pop', b'Pop'), (b'metal', b'Metal'), (b'altern', b'Alternative'), (b'indie', b'Indie')])),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bandprofile',
            name='website',
        ),
        migrations.RemoveField(
            model_name='fanprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='fanprofile',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='fanprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='fanprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='fanprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='bandprofile',
            name='profile',
            field=models.OneToOneField(default='', to='webapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fanprofile',
            name='profile',
            field=models.OneToOneField(default='', to='webapp.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='webapp.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(to='webapp.UserProfile'),
            preserve_default=True,
        ),
    ]
