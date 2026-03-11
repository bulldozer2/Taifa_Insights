from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('methodology/', views.methodology, name='methodology'),
    path('contact/', views.contact, name='contact'),
]
