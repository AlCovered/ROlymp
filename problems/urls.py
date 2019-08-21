from django.urls import path
from .views import *

urlpatterns = [
    path('problems_list/', problems_list, name='problems_list_url'),
    path('problem/<int:some_id>/', problem_itself, name='problem_url'),
    path('problem/create/', CreateProblem.as_view(), name='problem_create_url')
]