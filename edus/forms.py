from django.forms import forms, ModelForm
from . models import Question


class EditQuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'content']

