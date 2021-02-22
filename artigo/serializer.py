from django.db import models
from django.db.models import fields
from rest_framework import serializers
from artigo.models import Artigo, Categoria
from django.contrib.auth.models import User


class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ListaArtigoPublicadoAtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'
