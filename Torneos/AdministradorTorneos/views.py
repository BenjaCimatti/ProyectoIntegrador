from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, QuarterMatchForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
import random

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

    sm1.player1 = qm1.winner
    sm1.player2 = qm2.winner
    sm1.save()

    sm2.player1 = qm3.winner
    sm2.player2 = qm4.winner
    sm2.save()

    fm.player1 = sm1.winner
    fm.player2 = sm2.winner
    fm.save()


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


    def playerOne():
        qm1.player1 = player
        qm1.save()
        

    def playerTwo():
        qm1.player2 = player
        qm1.save()
        

    def playerThree():
        qm2.player1 = player
        qm2.save()
        

    def playerFour():
        qm2.player2 = player
        qm2.save()
        

    def playerFive():
        qm3.player1 = player
        qm3.save()
        

    def playerSix():
        qm3.player2 = player
        qm3.save()
        
        
    def playerSeven():
        qm4.player1 = player
        qm4.save()
        

    def playerEight():
        qm4.player2 = player
        qm4.save()

    
    playerOptions = {
        1 : playerOne,
        2 : playerTwo,
        3 : playerThree,
        4 : playerFour,
        5 : playerFive,
        6 : playerSix,
        7 : playerSeven,
        8 : playerEight,
    }

    def matchOne():
        if qm1.player1 == None:
            playerOptions[1]()
        else:
            playerOptions[2]()


    def matchTwo():
        if qm2.player1 == None:
            playerOptions[3]()
        else:
            playerOptions[4]()


    def matchThree():
        if qm3.player1 == None:
            playerOptions[5]()
        else:
            playerOptions[6]()


    def matchFour():
        if qm4.player1 == None:
            playerOptions[7]()
        else:
            playerOptions[8]()


    matchOptions = {
        0 : matchOne,
        1 : matchTwo,
        2 : matchThree,
        3 : matchFour,
    }

    
    form = QuarterMatchForm()
    if request.method == 'POST':
        flag = True
        while flag:

            randomMatch = random.randint(0, 3)
            if qm[randomMatch].player1 == None or qm[randomMatch].player2 == None:
                matchOptions[randomMatch]()
            
                flag = False

        return redirect('ver_torneos')
            

    context = {'tournaments': tournaments, 'qm1': qm1, 'qm2': qm2, 'qm3': qm3, 'qm4': qm4, 'sm1':sm1, 'sm2':sm2, 'fm': fm, 'user_id':user_id, 'deactivateBtn':deactivateBtn}
    return render(request, 'AdministradorTorneos/dynamic_tournament.html', context)
