# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2, choices=[(b'RG', b'Rate a gig'), (b'WG', b'Went to a gig'), (b'LC', b'Left a comment')])),
                ('xp', models.IntegerField(default=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BandProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('views', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=2, choices=[(b'GL', b'Glasgow'), (b'ED', b'Edinburgh'), (b'AB', b'Aberdeen'), (b'LO', b'London'), (b'DU', b'Dundee')])),
                ('genre', models.CharField(max_length=16, choices=[(b'rock', b'Rock'), (b'pop', b'Pop'), (b'metal', b'Metal'), (b'altern', b'Alternative'), (b'indie', b'Indie')])),
                ('mood', models.TextField(max_length=256)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('city', models.CharField(max_length=2, choices=[(b'GL', b'Glasgow'), (b'ED', b'Edinburgh'), (b'AB', b'Aberdeen'), (b'LO', b'London'), (b'DU', b'Dundee')])),
                ('venue', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('band', models.ForeignKey(to='webapp.BandProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FanProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xp', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=2, choices=[(0, b'Novice'), (1, b'Real Fan')])),
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
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField(max_length=1024)),
                ('band', models.ForeignKey(to='webapp.BandProfile')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='webapp.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='achievement',
            name='fan',
            field=models.ForeignKey(to='webapp.FanProfile'),
            preserve_default=True,
        ),
    ]
