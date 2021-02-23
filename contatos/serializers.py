from django.db.models import fields
from rest_framework import serializers

from contatos.models import Contato
from contatos.validators import *


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"})
        if not telefone_valido(data['telefone']):
            raise serializers.ValidationError(
                {'telefone': "O número de telefone deve respeitar o modelo (XX) XXXX-XXXX"})
        return data
