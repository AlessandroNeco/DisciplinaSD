from django.urls import path
from . import views


urlpatterns = [
    path('index.html', views.index),
    path('show.html', views.showMonografia),
    path('editar.html/<int:id>', views.editarMonografia),
    path('atualizar/<int:id>', views.atualizarMonografia),
    path('delete/<int:id>', views.deletarMonografia),
    
]
