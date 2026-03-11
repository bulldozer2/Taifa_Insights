from django.urls import path
from . import views

app_name = 'dashboards'

urlpatterns = [
    path('', views.dashboards_home, name='home'),
    path('<slug:slug>/', views.indicator_dashboard, name='indicator_dashboard'),
    path('<slug:slug>/data/', views.indicator_datapoints_api, name='indicator_data_api'),
]
