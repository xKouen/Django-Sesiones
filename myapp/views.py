from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login.html')
def recuperarContraseña(request):
    return render(request, 'recuperarContraseña.html')
def listaUsuarios(request):
    return render(request, 'listaUsuarios.html')
def listaAdmin(request):
    return render(request, 'listaAdmin.html')
def registrarUsuarios(request):
    return render(request, 'registrarUsuarios.html')