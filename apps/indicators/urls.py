from django.urls import path
from django.shortcuts import render

app_name = 'indicators'

urlpatterns = [
    path('', lambda request: render(request, 'indicators/index.html'), name='indicators'),
]
