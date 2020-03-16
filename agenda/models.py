from django.db import models
from django.utils import timezone

# Create your models here.

class locatarioModel(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=200, null=True, blank=True)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    
    dataCadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome


class locadorModel(models.Model):
    id = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=200, null=True, blank=True)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    
    dataCadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class apartamentoModel(models.Model):
    id = models.AutoField(primary_key=True)

    rua = models.CharField(max_length=1000, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=1000, null=True, blank=True)
    cidade = models.CharField(max_length=1000, null=True, blank=True)
    estado = models.CharField(max_length=1000, null=True, blank=True)
    valorDiaria = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    dataCadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.__str__(id)

class agendamentosModel(models.Model):
    PG = (
        ('1', 'Pago'),
        ('2', 'Não Pago'),
    )
    id = models.AutoField(primary_key=True)    

    estadoPagamento = models.CharField(max_length=1, choices=PG, default=1)
    apartamento = models.CharField(max_length=200, null=True, blank=True)
    locatario = models.CharField(max_length=200, null=True, blank=True)
    quantidadePessoas = models.CharField(max_length=200, null=True, blank=True)
    dataEntrada = models.DateTimeField(default=timezone.now)
    dataSaida = models.DateTimeField(default=timezone.now)    
    valorTotal = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    dataCadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email