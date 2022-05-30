#  hello/urls.py

from django.shortcuts import render

from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name='home'),
    path('quizz', views.quizzview, name='quizz'),
    path('projetos', views.quizzview, name='projetos'),
]
