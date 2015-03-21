from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from webapp.data_choices import TITLES, ACHIEVEMENTS, CITIES, GENRES

class Rating():

    def __init__(self):
        self.rating_sum = 0.0
        self.total = 0
        self.average_rating = 0.0
        self.all_ratings = {}

    def get(self, user):
        if user not in self.all_ratings:
            return None
        return self.all_ratings[user]

    def add(self, user, rating):
        self.all_ratings[user] = rating
        self.total += 1
        self.rating_sum += rating
        self.average_rating = self.rating_sum / self.total


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
    views = models.IntegerField(default=0)
    mood = models.TextField(max_length=256)
    rating = Rating()

    def __unicode__(self):
        return self.profile.user.username


class FanProfile(models.Model):
    profile = models.OneToOneField(UserProfile)
    xp = models.IntegerField(default=0)
    title = models.CharField(max_length=32)
    mood = models.TextField(max_length=256)
        
    def __unicode__(self):
        return self.profile.user.username


class Event(models.Model):
    band = models.ForeignKey(BandProfile) # Events are created by bands.
    name = models.CharField(max_length=128, unique=True)
    price = models.FloatField(default=0.0)
    rating = Rating()
    city = models.CharField(max_length=32)
    venue = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
	

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name


class Achievement(models.Model):
    fan = models.ForeignKey(FanProfile)
    name = models.CharField(max_length=16)
    xp = models.IntegerField(default=5)

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