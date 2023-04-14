from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recuperarContraseña/', views.recuperarContraseña, name="recuperarContraseña"),
    path('listaAdmin/', views.listaAdmin, name="listaAdmin"),
    path('registroUsuarios/', views.registrarUsuarios, name="registroUsuarios"),
    path('listaUsuarios/', views.listaUsuarios, name="listaUsuarios"),
    
]
    
