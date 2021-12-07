from os import name
from typing import AsyncIterable
from django import forms
from django.db import models
from django.db.models.enums import Choices
from django.forms import widgets
from django.forms.widgets import Widget
from settings import DEFAULT_AUTO_FIELD

# Create your models here.
#Definicao dos Metadados
class Monografia(models.Model):
    FORMATOS_ARQUIVOS_CHOICES = [
    ('PDF', 'PDF'),
    ('WORD', 'WORD'),
    ('ZIP', 'ZIP'),
]
    Titulo = models.CharField(max_length=300, blank=False)
    Autor = models.CharField(max_length=300, blank=False)
    Orientador = models.CharField(max_length=300, blank=False)
    Curso = models.CharField(max_length=300, blank=False)
    Universidade = models.CharField(max_length=300, blank=False)
    Area = models.CharField(max_length=100, blank=False)
    Formato = models.CharField(max_length=100, choices=FORMATOS_ARQUIVOS_CHOICES, blank=False)
    Numero_de_Paginas = models.IntegerField(blank=False)
    Data = models.DateField(null=False, blank=False)
    Banca = models.CharField(max_length=300, blank=False)
    Url = models.CharField(max_length=300, blank=False)

    class Meta:
        db_table="repositoriodemonografias"

    def __str__(self):
        return self.Titulo