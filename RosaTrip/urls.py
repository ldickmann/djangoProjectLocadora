from django.apps import AppConfig


# Criação das rotas, através do método path, que direcionam as requisições para as views correspondentes.
class RosatripConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RosaTrip'