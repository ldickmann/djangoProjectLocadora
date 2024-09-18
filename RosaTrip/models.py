from django.db import models


# Classe para cadastrar marcas dos veículos, cria o modelo de tabela no banco de dados.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# Classe para cadastrar veículos, cria o modelo de tabela no banco de dados.
class Veiculo(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='marca_veiculo')
    ano_fabricacao = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='RosaTrip/', null=True, blank=True)

    def __str__(self):
        return self.modelo
