from os import name
from typing import AsyncIterable
from django import forms
from django.db import models
from settings import DEFAULT_AUTO_FIELD

# Create your models here.
class Monografia(models.Model):
    Titulo = models.CharField(max_length=300)
    Autor = models.CharField(max_length=300)
    Orientador = models.CharField(max_length=300)
    Curso = models.CharField(max_length=300)
    Universidade = models.CharField(max_length=300)
    Area = models.CharField(max_length=100)
    Formato = models.CharField(max_length=10)
    Numero_de_Paginas = models.IntegerField()
    Data = models.DateField(max_length=10)
    Banca = models.CharField(max_length=300)
    Url = models.CharField(max_length=300)

    class Meta:
        db_table="repositoriodemonografias"
    
    def _str_(self):
        return self.Titulo

