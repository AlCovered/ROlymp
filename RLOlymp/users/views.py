from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth import views as AuthView
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from .forms import *
from .models import *

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

        if request.POST.get('Add') == 'Add':
            user_id = request.user.id
            user = Profile.objects.get(id=user_id)

            user.rank += 5
            user.save()

        data = {
            'title': 'Profile - RLOlymp',
        }

        return render(request, 'users/profile.html', data)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

class UpdateProfile(View):
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)

        data = {
            'title': 'Update Profile - RLOlymp',
            'form': form
        }

        return render(request, 'users/update_profile.html', data)

    def post(self, request):
        form = UpdateProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('profile_users_url')

        data = {
            'title': 'Update Profile - RLOlymp',
            'form': form
        }

        return render(request, 'users/update_profile.html', data)

class UpdatePassword(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)

        data = {
            'title': 'Update Password - RLOlymp',
            'form': form
        }

        return render(request, 'users/update_password.html', data)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST ,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('profile_users_url')
        else:
            return redirect('update_password_users_url')

        data = {
            'title': 'Updata Password - RLOlymp',
            'form': form
        }

        return render(request, 'users/update_password.html', data)

class DeleteUser(View):
    def get(self, request, username):
        user_del = User.objects.get(username__iexact=username)

        data = {
            'title': 'Delete User - RLOlymp',
            'user_del': user_del
        }

        return render(request, 'users/delete_user.html', data)

    def post(self, request, username):
        user_del = User.objects.get(username__iexact=username)
        user_del.delete()

        return redirect(reverse('home'))
