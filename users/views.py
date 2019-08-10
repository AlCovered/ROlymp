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


def user_list(request):
    users = User.objects.order_by('first_name')

    context = {'title': 'Users - RLOlymp', 'users': users}
    return render(request, 'users/users_list.html', context)


class Register(View):
    def get(self, request):
        form = UserRegistration()

        context = {'title': 'Registration - RLOlymp', 'form': form}
        return render(request, 'users/registration.html', context)

    def post(self, request):
        form = UserRegistration(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} successfully registered')

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('profile_users_url')

        context = {'title': 'Registration - RLOlymp','form': form}
        return render(request, 'users/registration.html', context)


class ProfileView(View):
    def get(self, request):
        context = {'title': 'Profile - RLOlymp',}
        return render(request, 'users/profile.html', context)

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

        context = {'title': 'Profile - RLOlymp'}
        return render(request, 'users/profile.html', context)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)


class UpdateProfile(View):
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)

        context = {'title': 'Update Profile - RLOlymp', 'form': form}
        return render(request, 'users/update_profile.html', context)

    def post(self, request):
        form = UpdateProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_users_url')

        context = {'title': 'Update Profile - RLOlymp', 'form': form}
        return render(request, 'users/update_profile.html', context)


class UpdatePassword(View):
    def get(self, request):
        form = PasswordChangeForm(user=request.user)

        context = {'title': 'Update Password - RLOlymp', 'form': form}
        return render(request, 'users/update_password.html', context)

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile_users_url')
        else:
            return redirect('update_password_users_url')

        context = {'title': 'Update Password - RLOlymp', 'form': form}
        return render(request, 'users/update_password.html', context)


class DeleteUser(View):
    def get(self, request, username):
        user_del = User.objects.get(username__iexact=username)

        context = {'title': 'Delete User - RLOlymp', 'user_del': user_del}
        return render(request, 'users/delete_user.html', context)

    def post(self, request, username):
        user_del = User.objects.get(username__iexact=username)
        user_del.delete()

        return redirect(reverse('home'))


class EditImageUser(View):
    def get(self, request):
        user_get = Profile.objects.get(user=request.user)
        form = EditImageForm(instance=user_get)

        context = {'title': 'Edit Profile - RLOlymp', 'form': form}
        return render(request, 'users/edit_profile.html', context)

    def post(self, request):
        user_get = Profile.objects.get(user=request.user)
        form = EditImageForm(request.POST, request.FILES, instance=user_get)

        if form.is_valid():
            form.save()
            return redirect('profile_users_url')

        context = {'title': 'Edit Profile - RLOlymp', 'form': form}
        return render(request, 'users/edit_profile.html', context)