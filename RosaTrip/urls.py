from django.urls import path
from . import views


# Criação das rotas, através do método path, que direcionam as requisições para as views correspondentes.
urlpatterns = [
    path('', views.index, name='index.html'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/cadastro/', views.cadastro, name='cadastro'),
    path('veiculos/', views.lista_veiculos, name='veiculos'),
    path('add-veiculo/', views.add_veiculo, name='add_veiculo'),
    path('edit-veiculo/<int:pk>/', views.edit_veiculo, name='edit_veiculo'),
    path('del-veiculo/<int:pk>/', views.del_veiculo, name='del_veiculo'),
]