from datetime import date

from django.core.exceptions import ViewDoesNotExist
from django.db.models.query import QuerySet
from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from artigos.models import Artigo, Categoria
from artigos.serializer import (ArtigoSerializer, CategoriaSerializer,
                               ListaArtigoPublicadoAtivoSerializer)


class ArtigoViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os Artigos"""
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    """ Exibindo todas as categorias """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaArtigoPublicadoAtivoViewSet(generics.ListAPIView):
    """ Lista todos os artigos que estão ativos e com data de publicação inferior ao dia atual"""

    def get_queryset(self):
        data_inicial = "0001-01-01"
        data_final = date.today()
        queryset = Artigo.objects.filter(ativo=True).filter(
            data_publicacao__range=[data_inicial, data_final])
        return queryset
    serializer_class = ListaArtigoPublicadoAtivoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
