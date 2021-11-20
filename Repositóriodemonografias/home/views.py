
from django.contrib import messages
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
            return render(request, 'index.html', {'form':form})
        else:
            messages.sucess(request, 'Erro ao salvar os dados!')
            return redirect('index')
    form = MonografiaForm()
    return render(request, 'index.html', {'form':form})
