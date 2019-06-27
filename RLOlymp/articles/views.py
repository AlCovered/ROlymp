from django.shortcuts import render, redirect
from django.views.generic import View

from .models import *
from .forms import *

# Create your views here.
class Articles(View):
    def get(self, request):
        article = Article.objects.all()[::-1]

        data = {
            'title': 'Articles - RLOlymp',
            'article': article
        }

        return render(request, 'articles/articles.html', data)

class ArticleCreate(View):
    def get(self, request):
        form = ArticleForm()

        data = {
            'title': 'Article Create Form - RLOlymp',
            'form': form
        }

        return render(request, 'articles/article_create_form.html', data)

    def post(self, request):
        bound_form = ArticleForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('articles_url')

        data = {
            'title': 'Article Create Form - RLOlymp',
            'form': bound_form
        }

        return render(request, 'articles/article_create_form.html', data)