from django.db import models
from django.contrib.auth.models import User

class BandProfile(models.Model):
    user = models.OneToOneField(User)
    views = models.IntegerField(default=0)
    city = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.user.username


class Event(models.Model):
    band = models.ForeignKey(BandProfile)
    price = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)
    location = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
        
    def __unicode__(self):
        return self.name


class FanProfile(models.Model):
    user = models.OneToOneField(User)
    xp = models.IntegerField(default=0)
    title = models.CharField(max_length=128)
    mood = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
        
    def __unicode__(self):
        return self.user.username


class Achievement(models.Model):
    xp = models.IntegerField(default=0)
    name = models.CharField(max_length=128)


class Comment(models.Model):
    rating = models.FloatField(default=0.0)
    review = models.TextField(max_length=128)