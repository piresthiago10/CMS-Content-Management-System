from typing import TextIO

from django.db import models


class Contato(models.Model):
    nome = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, max_length=100)
    telefone = models.CharField(max_length=15)
    whatsapp = models.BooleanField()
    telegram = models.BooleanField()
    assunto = models.CharField(blank=False, max_length=140)
    texto = models.TextField(blank=False)
    respondido = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.assunto
