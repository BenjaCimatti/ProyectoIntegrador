from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'AdministradorTorneos/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'AdministradorTorneos/login.html', context)