from django.db import models
#import abstract user
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user (AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ['username', 'email']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class forma_pagamento(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

class despesa(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=150)
    forma_pagamento = models.ForeignKey(forma_pagamento, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
