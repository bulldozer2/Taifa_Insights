from django.urls import path
from django.shortcuts import render

app_name = 'datasets'

urlpatterns = [
    path('', lambda request: render(request, 'datasets/index.html'), name='datasets'),
]
