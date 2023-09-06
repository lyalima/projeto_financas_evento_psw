from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('cadastrar_conta_banco', views.cadastrar_conta_banco, name='cadastrar_conta_banco'),
]