from django.shortcuts import render
from django.views.generic import View

class Home(View):
    def get(self, request):
        data = {
            'title': 'Home - RLOlymp'
        }

        return render(request, 'index.html', data)