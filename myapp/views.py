from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse('Este es el index')
def recuperarContraseña(request):
    return render(request, 'recuperarContraseña')
def listaUsuarios(request):
    return render(request, 'listaUsuarios')
def listaAdmin(request):
    return render(request, 'listaAdmin')
def registrarUsuarios(request):
    return render(request, 'registrarUsuarios')