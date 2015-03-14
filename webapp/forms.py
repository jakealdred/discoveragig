from django import forms
from django.contrib.auth.models import User
from webapp.models import BandProfile, FanProfile




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class BandProfileForm(forms.ModelForm):
    class Meta:
        model = BandProfile
        fields = ('city', 'genre')


class FanProfileForm(forms.ModelForm):
    class Meta:
        model = FanProfile
        fields = ('city', 'genre', 'mood')
