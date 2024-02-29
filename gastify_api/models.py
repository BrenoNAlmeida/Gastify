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