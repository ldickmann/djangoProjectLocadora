from django.contrib import admin
from django.urls import path
import RosaTrip.views
from accounts.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', RosaTrip.views.home, name='index'),
    path('contato/', RosaTrip.views.contato, name='contato'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('veiculos/', RosaTrip.views.VeiculosListView.as_view(), name='frota'),
    path('add-veiculo/', RosaTrip.views.VeiculoCreateView.as_view(), name='add-veiculo'),
    path('veiculo/<int:pk>/', RosaTrip.views.VeiculoDetailView.as_view(), name='detalhe'),
    path('veiculo/<int:pk>/editar/', RosaTrip.views.VeiculoUpdateView.as_view(), name='edit-veiculo'),
    path('veiculo/<int:pk>/deletar/', RosaTrip.views.VeiculoDeleteView.as_view(), name='del-veiculo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
