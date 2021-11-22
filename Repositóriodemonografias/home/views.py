
from django.contrib import messages
from django.contrib.messages.api import error
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from .models import Monografia

from home.forms import MonografiaForm

# Create your views here.
def index(request):
    monografia = Monografia.objects.all()
    if request.method=='POST':
        form = MonografiaForm(request.POST)
        if form.is_valid():
            form.save()
            print('Dados salvos com sucesso!!!')
            form.cleaned_data
            #return render(request, 'index.html', {'form':form})
        else:
            print('Erro ao salvar os dados!')
            #messages.error(request, "Error")
            return render(request, 'index.html', {'form':form})
    form = MonografiaForm()
    return render(request, 'index.html', {'form':form})
