from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from webapp.data_choices import CITIES, GENRES
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.user.username


class BandProfile(models.Model):
    profile = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return self.profile.user.username


class FanProfile(models.Model):
    profile = models.OneToOneField(UserProfile)
    xp = models.IntegerField(default=0)
    title = models.CharField(max_length=32)
        
    def __unicode__(self):
        return self.profile.user.username


class Event(models.Model):
    band = models.ForeignKey(BandProfile) # Events are created by bands.
    name = models.CharField(max_length=128, unique=True)
    date = models.DateField(("Date"), default=datetime.date.today, null=True, blank=True)
    city = models.CharField(max_length=32)
    venue = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    genre = models.CharField(max_length=32)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name


class Achievement(models.Model):
    fan = models.ForeignKey(FanProfile)
    name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    date = models.DateField(default=timezone.now)
    text = models.TextField(max_length=1024)


class Feedback(models.Model):
    user = models.ForeignKey(UserProfile)
    band = models.ForeignKey(BandProfile)
    date = models.DateField(default=timezone.now)
    text = models.TextField(max_length=1024)
