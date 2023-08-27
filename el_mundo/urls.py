from django.contrib import admin
from django.urls import path

from el_mundo import views

urlpatterns = [
    path('', views.view_homepage, name='world_map'),
    path('all_data/', views.all_data),
    path('country/<str:country_name>/', views.country_info, name='country_info'),
    # path('currency/', views.currency),
    # path('languages/', views.languages),
    path('login/', views.login)
]