from django.urls import path
from . import views

app_name = 'insights'

urlpatterns = [
    path('', views.list_insights, name='list'),
    path('<slug:slug>/', views.detail_insight, name='detail'),
]
