from django import forms
from .models import *

class MonografiaForm(forms.ModelForm):
    class Meta:
        model = Monografia
        fields = ["Titulo", "Autor", "Orientador", "Curso", "Universidade","Area", 
        "Formato", "Numero_de_Paginas", "Data", "Banca", "Url"]