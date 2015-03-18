from django import forms
from django.contrib.auth.models import User
from webapp.models import BandProfile, FanProfile, Event, Comment, Feedback


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class BandProfileForm(forms.ModelForm):
    class Meta:
        model = BandProfile
        fields = ('name', 'city', 'genre', 'picture', 'mood', 'website')


class FanProfileForm(forms.ModelForm):
    class Meta:
        model = FanProfile
        fields = ('city', 'genre', 'picture', 'website')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'city', 'website', 'picture', 'price', 'venue')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('text',)
        
            
