from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    return render(request, 'registration/login.html', {

    })
