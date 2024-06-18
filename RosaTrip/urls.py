from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/cadastro/', views.cadastro, name='cadastro'),
    path('veiculos/', views.lista_veiculos, name='veiculos'),
    path('add-veiculo/', views.add_veiculo, name='add_veiculo'),
    path('edit-veiculo/<int:pk>/', views.edit_veiculo, name='edit_veiculo'),
    path('del-veiculo/<int:pk>/', views.del_veiculo, name='del_veiculo'),
]
