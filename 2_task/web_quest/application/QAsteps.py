from django import forms
from .models import Question, Answer


class AddQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('topic', 'text')

class AddAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('question', 'text')
