from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from equiz.models import Section, Question, Answer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('title', 'category', 'description', 'video_url')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('quiz_type', 'question', 'markerTime', 'replayTime', 'value', 'penalty', 'feedback', 'hint')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', 'is_answer_correct')


QuestionFormSet = inlineformset_factory(Question, Answer)