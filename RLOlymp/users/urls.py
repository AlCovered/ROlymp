from django.urls import path

from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register_url'),
    path('login/', AuthView.LoginView.as_view(template_name='users/sign_in.html', extra_context={'title': 'Sign In - RLOlymp'}), name='sign_in_users_url'),
    path('logout/', AuthView.LogoutView.as_view(template_name='users/sign_out.html', extra_context={'title': 'Sign Out - RLOlymp'}), name='sign_out_users_url'),
    path('profile/', ProfileView.as_view(), name='profile_users_url'),
    path('profile/update', UpdateProfile.as_view(), name='profile_update_users_url'),
    path('profile/delete/<str:username>', DeleteUser.as_view(), name='profile_delete_users_url'),
    path('password/', UpdatePassword.as_view(), name='update_password_users_url'),
    path('all-users/', UserList.as_view(), name='users_list_url'),
]