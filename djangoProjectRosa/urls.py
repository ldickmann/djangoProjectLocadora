from django.contrib import admin
from django.urls import path, include
from . import views
from accounts.views import register_view, login_view, logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', include('RosaTrip.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
