from django import forms
from django.contrib.auth.models import User
from webapp.models import UserProfile, FanProfile, BandProfile, Event, Comment, Feedback


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'city', 'genre', 'picture', 'website')


class BandProfileForm(forms.ModelForm):
    class Meta:
        model = BandProfile
        fields = ('mood',)


class FanProfileForm(forms.ModelForm):
    class Meta:
        model = FanProfile
        fields = ('mood',)


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
        
            
