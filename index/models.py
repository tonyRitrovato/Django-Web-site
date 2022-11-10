from django.db import models

# Create your models here.

class Registrazione(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    numeroBiglietti = models.IntegerField(default=0)

    def __str__(self):
        return self.email

