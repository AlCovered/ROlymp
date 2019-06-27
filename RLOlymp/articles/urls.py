from django.urls import path

from .views import *

urlpatterns = [
    path('', Articles.as_view(), name='articles_url'),
    path('create/', ArticleCreate.as_view(), name='articles_create_url')
]