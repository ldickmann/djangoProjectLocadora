from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('test-login/', views.test_login, name='test_login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista_veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path('add_veiculo/', views.add_veiculo, name='add_veiculo'),
    path('edit_veiculo/<int:pk>/', views.edit_veiculo, name='edit_veiculo'),
    path('del_veiculo/<int:pk>/', views.del_veiculo, name='del_veiculo'),
]
