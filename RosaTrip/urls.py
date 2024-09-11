from django.urls import path
from . import views


urlpatterns = [
    path('veiculos/', views.VeiculosListView.as_view(), name='frota'),
    path('add-veiculo/', views.VeiculoCreateView.as_view(), name='add-veiculo'),
    path('veiculo/<int:pk>/', views.VeiculoDetailView.as_view(), name='detalhe'),
    path('veiculo/<int:pk>/editar/', views.VeiculoUpdateView.as_view(), name='edit-veiculo'),
    path('veiculo/<int:pk>/deletar/', views.VeiculoDeleteView.as_view(), name='del-veiculo'),
]
