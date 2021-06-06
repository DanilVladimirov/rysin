from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from siterysin.models import Publication, FeedBack


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['photo']


class FormRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
