from django.contrib import admin
from django.urls import path

from el_mundo import views

urlpatterns = [
    # path('', views.hola, name='hola'),
    path('', views.index, name='world_map')
]