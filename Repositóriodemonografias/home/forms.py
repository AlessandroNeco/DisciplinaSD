from django import forms
from django.db.models.expressions import Window
from django.db.models.fields import DateField
from django.forms import widgets
from .models import *



class MonografiaForm(forms.ModelForm):
    Data = forms.DateField(widget=widgets.NumberInput(attrs={'type': 'date'}))
 
    #Data = forms.DateField(widget=widgets.SelectDateWidget()
    class Meta:
        model = Monografia
        #Metadados que apareceram na pagina e serao salvos
        #fields = ["Titulo", "Autor", "Orientador", "Curso", "Universidade","Area", 
        #"Formato", "Numero_de_Paginas", "Data", "Banca", "Url"]
        
        fields = '__all__'
