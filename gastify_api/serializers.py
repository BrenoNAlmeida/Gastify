# define os serializer da aplicação
# """
# from rest_framework import serializers
from .models import *
from rest_framework import serializers


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ["id", "username", "email"]


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = forma_pagamento
        fields = ["id", "nome", "tipo"]


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = despesa
        fields = ["id", "nome", "valor", "data", "forma_pagamento", "usuario"]
