from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('<slug:id_>/', views.author, name='author'),
]
