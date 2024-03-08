from django.db import models

# import abstract user
from django.contrib.auth.models import AbstractUser


# Create your models here.
class usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ["username", "email"]
    USERNAME_FIELD = "email"

   # Adicione ou altere o related_name para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    def __str__(self):
        return self.email


class forma_pagamento(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)  # credito, debito, dinheiro, pix, boleto
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class despesa(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    forma_pagamento = models.ForeignKey(forma_pagamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome