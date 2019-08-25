from django.urls import path
from .views import *

urlpatterns = [
    path('problems_list/', problems_list, name='problems_list_url'),
    path('problem/<int:some_id>/', problem_itself, name='problem_url'),
    path('problem/create/', CreateProblem.as_view(), name='problem_create_url'),
    path('problem/<int:some_id>/send_decision/', SendDecision.as_view(), name='problem_send_decision_url'),
    path('problem/<int:some_id>/correct_answer', correct_answer, name='correct_answer_url'),
    path('problem/<int:some_id>/incorrect_answer', incorrect_answer, name='incorrect_answer_url')
]
