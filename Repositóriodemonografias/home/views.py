
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
            return redirect('/show')
            
            #return render(request, 'index.html', {'form':form})
        else:
            print('Erro ao salvar os dados!')
            #messages.error(request, "Error")
            form = MonografiaForm()
            return render(request, 'index.html', {'form':form})
    form = MonografiaForm()
    return render(request, 'index.html', {'form':form})

def showMonografia(request):  
    mostrar = Monografia.objects.all()  
    return render(request,"show.html",{'mostar':mostrar})  

def editarMonografia(request, id):  
    editarMono = Monografia.objects.get(id=id)  
    return render(request,'editar.html', {'editarMono':editarMono})  

def atualizarMonografia(request, id):  
    atualizarMono = Monografia.objects.get(id=id)  
    form = MonografiaForm(request.POST, instance = atualizarMono)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'atualizar.html', {'atualizarMono': atualizarMono})  

def deletarMonografia(request, id):  
    deletarMono = Monografia.objects.get(id=id)  
    deletarMono.delete()  
    return redirect("/show")