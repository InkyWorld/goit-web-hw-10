from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page_number>/', views.main, name='main_paginate'),
    path('add-author/', views.add_author, name='add-author'),
    path('add-quote/', views.add_quote, name='add-quote'),
]
