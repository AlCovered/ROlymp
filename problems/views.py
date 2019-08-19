from django.shortcuts import render
from .models import *


def problems_list(request):
    condition = Condition.objects.all()

    context = {'title': 'Problems - RLOlymp', 'condition': condition}
    return render(request, 'problems/problems_list.html', context)


def problem_itself(request, some_id):
    condition_one = Condition.objects.get(id=some_id)

    context = {'title': condition_one.title + ' - RLOlymp', 'condition_one': condition_one}
    return render(request, 'problems/problem.html', context)
