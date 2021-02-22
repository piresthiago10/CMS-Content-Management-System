from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=280)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=140)
    texto = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_criacao = models.DateField()
    data_publicacao = models.DateField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)
    ativo = models.BooleanField()

    def __str__(self):
        return self.titulo