from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Registrazione(models.Model):
    CHOICES = [(i,i) for i in range(11)]
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    numeroBiglietti = models.IntegerField(default=0,  choices=CHOICES)

    def __str__(self):
        return (self.nome)

