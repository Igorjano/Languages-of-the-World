from django.contrib import admin
from django.urls import path

from el_mundo import views

urlpatterns = [
    path('', views.view_homepage, name='home'),
    path('all_data/', views.all_data),
    path('country/<str:country_name>/', views.country_info, name='country_info'),
    # path('currency/', views.currency),
    # path('languages/', views.languages),
    path('countries/', views.countries_form_view),
    path('login/', views.sign_in),
    path('logout/', views.sign_out),
    path('signup/', views.sign_up)
]