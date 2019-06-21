from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', Register.as_view(), name='register_url'),
    path('login/', AuthView.LoginView.as_view(template_name='users/sign_in.html', extra_context={'title': 'Sign In - RLOlymp'}), name='sign_in_users_url'),
    path('logout/', AuthView.LogoutView.as_view(template_name='users/sign_out.html', extra_context={'title': 'Sign Out - RLOlymp'}), name='sign_out_users_url'),
    path('profile/', Profile.as_view(), name='profile_users_url')
]