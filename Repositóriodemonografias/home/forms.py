from django import forms
from .models import *

class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografia
        #Metadados que apareceram na pagina e serao salvos
        fields = ["Titulo", "Autor", "Orientador", "Curso", "Universidade","Area", 
        "Formato", "Numero_de_Paginas", "Data", "Banca", "Url"]
        #fields = '__all__'