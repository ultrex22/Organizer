from django import forms
from django.forms import ModelForm, Form
from .models import Notes


class AllNotesForm(ModelForm):
    class Meta:
        model = Notes
        exclude = ['slug', 'id']


