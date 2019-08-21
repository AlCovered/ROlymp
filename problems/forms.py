from django import forms
from .models import *


class CreateProblemForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['title', 'condition_itself', 'examples', 'explanation', 'memory_limit', 'time_limit']
