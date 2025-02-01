from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('logout/', views.logout, name='logout'),
]
