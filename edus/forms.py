from django.forms import forms, ModelForm
from . models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class EditQuestionForm(ModelForm):
#
#     class Meta:
#         model = Question
#         fields = ['title', 'content']
#




class SignUpForm(UserCreationForm):
    email = forms.Field(help_text='What is your email')

    #need to add email validator

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )