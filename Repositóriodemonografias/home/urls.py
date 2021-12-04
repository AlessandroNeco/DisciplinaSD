from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('show', views.showMonografia),
    path('editar/<int:id>', views.editarMonografia),
    path('atualizar/<int:id>', views.atualizarMonografia),
    path('delete/<int:id>', views.deletarMonografia),
    
]
