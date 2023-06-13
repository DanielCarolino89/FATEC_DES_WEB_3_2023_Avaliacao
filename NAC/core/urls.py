from django.urls import path
from . import views

urlpatterns = [
  path('', views.Cadastro, name='Cadastro'),
  path('Listar/', views.Listar, name='Listar'),
]
