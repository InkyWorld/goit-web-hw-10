from django.urls import path

from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('sign-up/', views.sign_in, name='sign-up'),
    path('logout/', views.logout_view, name='logout'),
]
