from django.db import models


class Cerveja(models.Model):
    nome = models.CharField(max_length=50, blank=True)
    marca = models.CharField(max_length=30, null=True, blank=True)
