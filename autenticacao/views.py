from django.shortcuts import render
from django.http import HttpResponse
from .utils import password_is_valid, name_is_valid, email_is_valid
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def register(request):
    if request.method != "POST":
        if request.user.is_authenticated:
            return redirect('/plataforma/home')
        return render(request, 'register.html')
    else:
        username = request.POST.get('name')  # Com a tag name do INPUT do HTML
        mail = request.POST.get('email')
        passw = request.POST.get('password')
        cpassw = request.POST.get('confirm-password')

        if not name_is_valid(request, username):
            return redirect('/auth/register')
        elif not email_is_valid(request, mail):
            return redirect('/auth/register')
        elif not password_is_valid(request, passw, cpassw):
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username,
                                            email=mail,
                                            password=passw,
                                            is_active=True)
            user.save()
            messages.add_message(request, constants.SUCCESS,
                                 'Usuário cadastrado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR,
                                 'Erro interno do sistema')
            return redirect('/auth/register')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/plataforma/home')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('pssw')
        usuario = auth.authenticate(username=username, password=senha)
    if not usuario:
        messages.add_message(request, constants.ERROR,
                             'Username ou senha inválidos')
        return redirect('/auth/login')
    else:
        auth.login(request, usuario)
        return redirect('/plataforma/home')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
