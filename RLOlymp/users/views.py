from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth import views as AuthView

from .forms import UserRegistration

class Home(View):
    def get(self, request):
        data = {
            'title': 'Home - RLOlymp'
        }

        return render(request, 'main.html', data)

class Register(View):
    def get(self, request):
        form = UserRegistration()

        data = {
            'title': 'Registraion - RLOlymp',
            'form': form
        }

        return render(request, 'users/registration.html', data)

    def post(self, request):
        form = UserRegistration(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} successfuly registred')

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)

            return redirect('register_url')

        data = {
            'title': 'Registration - RLOlymp',
            'form': form
        }

        return render(request, 'users/registration.html', data)

class Profile(View):
    def get(self, request):
        data = {
            'title': 'Profile - RLOlymp'
        }

        return render(request, 'users/profile.html', data)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Profile, self).dispatch(request, *args, **kwargs)
    
