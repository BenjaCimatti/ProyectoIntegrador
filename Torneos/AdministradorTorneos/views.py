from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, QuarterMatchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='login')
def homePage(request):
    return render(request, 'AdministradorTorneos/home.html')

def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
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
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'El usuario o la contraseña es incorrecto')

        context = {}
        return render(request, 'AdministradorTorneos/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def verTorneos(request):
    tournaments = Tournament.objects.all()
    return render(request, 'AdministradorTorneos/ver_torneos.html', {'tournaments': tournaments})

@login_required(login_url='login')
def Torneo(request, pk):


    tournaments = Tournament.objects.get(id=pk)

    qm = tournaments.quartermatch_set.all().order_by('matchNumber')
    qm1 = qm[0]
    qm2 = qm[1]
    qm3 = qm[2]
    qm4 = qm[3]

    sm = tournaments.semimatch_set.all().order_by('matchNumber')
    sm1 = sm[0]
    sm2 = sm[1]

    fm = FinalMatch.objects.get(tournament=tournaments)

    user_id = request.user.id
    player = Player.objects.get(id=user_id)

      

    countPlayer = 0
    deactivateBtn = None


    for i in range(4):
        if qm[i].player1 != None:
            countPlayer += 1
        else:
            deactivateBtn = False
            break
        if qm[i].player2 != None:
            countPlayer += 1
        else:
            deactivateBtn = False
            break
    
    if countPlayer == 8:
        deactivateBtn = True
        countPlayer = 0
    else:
        isP1 = qm.filter(player1=player)
        isP2 = qm.filter(player2=player)
        if isP1.exists() or isP2.exists():
            deactivateBtn = True
        else:
            deactivateBtn = False


    

    
    form = QuarterMatchForm()
    if request.method == 'POST':
        

        qm1.player1 = player
        qm1.save()
        return redirect('ver_torneos')
            

    context = {'tournaments': tournaments, 'qm1': qm1, 'qm2': qm2, 'qm3': qm3, 'qm4': qm4, 'sm1':sm1, 'sm2':sm2, 'fm': fm, 'user_id':user_id, 'deactivateBtn':deactivateBtn}
    return render(request, 'AdministradorTorneos/dynamic_tournament.html', context)
