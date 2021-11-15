from django.shortcuts import render

from home.forms import MonografiaForm

# Create your views here.
def index(request):
    form = MonografiaForm()
    return render(request, 'index.html', {'form':form})