from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page_number>', views.main, name='main_paginate'),
]
