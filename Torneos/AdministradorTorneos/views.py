from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def homePage(request):
    return render(request, 'AdministradorTorneos/home.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cuenta creada correctamente')
        return redirect('login')

    context = {'form':form}
    return render(request, 'AdministradorTorneos/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'AdministradorTorneos/login.html', context)