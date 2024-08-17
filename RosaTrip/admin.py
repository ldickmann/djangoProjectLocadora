from django.contrib import admin
from RosaTrip.models import Veiculo, Marca

# Registra os models no painel de administração.


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabricacao', 'ano_modelo', 'cor', 'placa', 'preco', 'disponivel', 'foto')
    search_fields = ('modelo', 'marca', )


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome', )


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Veiculo, VeiculoAdmin)