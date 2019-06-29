from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth import views as AuthView
from django.contrib.auth.models import User

from .forms import UserRegistration
from .models import *

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class UserList(View):
    def get(self, request):
        users = User.objects.all()

        data = {
            'title': 'Users - RLOlymp',
            'users': users
        }

        return render(request, 'users/users_list.html', data)

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

class ProfileView(View):
    def get(self, request):
        data = {
            'title': 'Profile - RLOlymp',
        }

        return render(request, 'users/profile.html', data)

    def post(self, request):
        if request.POST.get('Next') == 'Next':
            user_id = request.user.id
            user = Profile.objects.get(id=user_id)

            user.solved_problems += 1
            user.save()

        data = {
            'title': 'Profile - RLOlymp',
        }

        return render(request, 'users/profile.html', data)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)
