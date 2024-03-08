# define as urls da aplicação
# """
# URL configuration for conf project.
#

from django.urls import include, path
from rest_framework import routers
from .views import UsuarioViewSet, FormaPagamentoViewSet, DespesaViewSet

app_name = "gastify_api"

router = routers.DefaultRouter()
router.register(r"usuario", UsuarioViewSet)
router.register(r"forma_pagamento", FormaPagamentoViewSet)
router.register(r"despesa", DespesaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
