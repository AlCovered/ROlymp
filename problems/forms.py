from django import forms
from .models import *


class CreateProblemForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['title', 'condition_itself', 'examples', 'explanation', 'memory_limit', 'time_limit']


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['code_language', 'code_itself']
