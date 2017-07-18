from django.forms import forms, ModelForm
from . models import Question, Document
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.Field(help_text='What is your email')

    #need to add email validator

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)