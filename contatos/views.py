from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, views, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contatos.models import Contato
from contatos.serializers import ContatoSerializer


class ContatosViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['nome', 'telefone', 'email', 'assunto']
    ordering_fields = ['nome']
    filterset_fields = ['respondido']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
