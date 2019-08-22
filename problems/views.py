from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *
import requests


def problems_list(request):
    condition = Condition.objects.all()[::-1]

    context = {'title': 'Problems - RLOlymp', 'condition': condition}
    return render(request, 'problems/problems_list.html', context)


def problem_itself(request, some_id):
    condition_one = Condition.objects.get(id=some_id)

    context = {'title': condition_one.title + ' - RLOlymp', 'condition_one': condition_one}
    return render(request, 'problems/problem.html', context)


class SendDecision(View):
    def get(self, request, some_id):
        code_form = CodeForm()
        condition = Condition.objects.get(id=some_id)

        context = {'title': 'Send Decision - RLOlymp', 'code_form': code_form}
        return render(request, 'problems/solve_send.html', context)

    def post(self, request, some_id):
        code_form = CodeForm(request.POST)
        condition = Condition.objects.get(id=some_id)

        if code_form.is_valid():
            code_language = code_form.cleaned_data['code_language']
            code = code_form.cleaned_data['code_itself']

            url = 'https://rextester.com/rundotnet/api'
            to_compile = {
                'LanguageChoice': code_language,
                'Program': code,
                'Input': '',
                'CompilerArgs': ''
            }

            response = requests.post(url, params=to_compile)
            result_of_program = response.json()['Result'].strip()

            if result_of_program == condition.answer:
                return redirect('correct_answer_url')
            else:
                return redirect('incorrect_answer_url')

        context = {'title': 'Send Decision - RLOlymp', 'code_form': code_form}
        return render(request, 'problems/solve_send.html', context)


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


def correct_answer(request):
    context = {'title': 'Correct Answer - RLOlymp'}
    return render(request, 'problems/correct_answer.html', context)


def incorrect_answer(request):
    context = {'title': 'Incorrect Answer - RLOlymp'}
    return render(request, 'problems/incorrect_answer.html', context)


