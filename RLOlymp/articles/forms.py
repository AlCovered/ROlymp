from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'short_description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }