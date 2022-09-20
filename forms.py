from dataclasses import fields
from socket import fromshare
from django import forms
from .models import NewsLettersUser, NewsLetter

class NewsLetterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsLettersUser
        fields = ['email']


class NewsLetterCreationForm(forms.ModelForm):
    class Meta:
        model= NewsLetter
        fields = ['name','subject','body','email','status']