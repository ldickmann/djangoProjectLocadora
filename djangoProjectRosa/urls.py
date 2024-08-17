from django.contrib import admin
from django.urls import path, include
from RosaTrip.views import VeiculoCreateView, VeiculosListView, home, contato
from accounts.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='index'),
    path('contato/', contato, name='contato'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('veiculos/', VeiculosListView.as_view(), name='frota'),
    path('add-veiculo/', VeiculoCreateView.as_view(), name='add-veiculo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
