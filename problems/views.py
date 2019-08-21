from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *


def problems_list(request):
    condition = Condition.objects.all()[::-1]

    context = {'title': 'Problems - RLOlymp', 'condition': condition}
    return render(request, 'problems/problems_list.html', context)


def problem_itself(request, some_id):
    condition_one = Condition.objects.get(id=some_id)

    context = {'title': condition_one.title + ' - RLOlymp', 'condition_one': condition_one}
    return render(request, 'problems/problem.html', context)


class CreateProblem(View):
    def get(self, request):
        condition_form = CreateProblemForm()

        context = {'title': 'Create Problem - RLOlymp', 'condition_form': condition_form}
        return render(request, 'problems/create_problem.html', context)

    def post(self, request):
        condition_form = CreateProblemForm(request.POST)

        if condition_form.is_valid():
            condition_form.save()
            return redirect('problems_list_url')

        context = {'title': 'Create Problem - RLOlymp', 'condition_form': condition_form}
        return render(request, 'problems/create_problem.html', context)
