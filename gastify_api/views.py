from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import usuario, forma_pagamento, despesa
from .serializers import usuarioSerializer, FormaPagamentoSerializer, DespesaSerializer 
from django.http import HttpResponse
from rest_framework import status, viewsets

# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = forma_pagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = despesa.objects.all()
    serializer_class = DespesaSerializer
