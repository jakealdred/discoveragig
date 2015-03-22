from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile, FanProfile, BandProfile, Event, Comment, Feedback
from datetime import date
from datetime import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(required=False)
    city = forms.CharField(required=False)
    genre = forms.CharField(required=False)
    picture = forms.ImageField(required=False)
    website = forms.URLField(required=False)
    class Meta:
        model = UserProfile
        fields = ('name', 'city', 'genre', 'picture', 'website')


class BandProfileForm(forms.ModelForm):
    mood = forms.CharField(required=False)
    class Meta:
        model = BandProfile
        fields = ('mood',)


class FanProfileForm(forms.ModelForm):
    mood = forms.CharField(required=False)
    class Meta:
        model = FanProfile
        fields = ('mood',)

class EventForm(forms.ModelForm):
    city = forms.CharField(required=False)
    website = forms.URLField(required=False)
    venue = forms.CharField(required=False)
    picture = forms.ImageField(required=False)
    price = forms.FloatField(required=False)
    date = forms.DateField(required=False)
    genre = forms.CharField(required=False)
    class Meta:
        model = Event
        fields = ('name', 'city', 'website', 'picture', 'price', 'venue','date','genre')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('text',)
        
