from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from artigo.models import Artigo, Categoria
from artigo.validators import *


class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

    def validate(self, data):
        data_criacao = date.today()
        data_publicacao = data['data_publicacao']

        if not data_publicacao_valida(data_publicacao, data_criacao):
            raise serializers.ValidationError(
                {'data_publicacao': "A data de publicação deve ser maior ou igual do que a data de criação."})
        return data


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ListaArtigoPublicadoAtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'
