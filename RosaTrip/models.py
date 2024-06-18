from django.db import models
from django.contrib.auth.models import User


class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    placa = models.CharField(max_length=7, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano} {self.cor} {self.preco} {self.disponivel}"
