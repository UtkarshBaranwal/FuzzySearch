from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('autocomplete/', views.company_autocomplete, name='company_autocomplete'),

]