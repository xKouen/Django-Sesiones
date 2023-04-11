from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="index"),
    path('recuperarContraseña/', views.recuperarContraseña, name="recuperarConstraseña"),
    path('listaAdmin/', views.listaAdmin, name="listaAdmin"),
    path('registroUsuarios/', views.registrarUsuarios, name="registroUsuarios"),
    path('listaUsuarios/', views.listaUsuarios, name="listaUsuarios"),
    
]
    
