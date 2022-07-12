from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Imovel_dois, Comentarios, Share
from django.contrib import messages
import datetime
# Create your views here.


@login_required(login_url='/auth/login')
def home(request):
    if request.method == "GET":
        # imoveis = Imovel_dois.objects.filter()
        imoveis = Imovel_dois.objects.all()
        context = {'imoveis': imoveis, 'user': request.user}
    return render(request, 'home.html', context)


@login_required(login_url='/auth/login')
def cad_imoveis(request):
    if request.method == "GET":
        return render(request, 'cad_imoveis.html')
    elif request.method == "POST":
        propriedade = Imovel_dois()

        propriedade.bairro = request.POST.get('endereco')
        propriedade.descricao = request.POST.get('descricao')
        propriedade.valor = request.POST.get('house-price')
        propriedade.nquartos = request.POST.get('Quartos')
        propriedade.nbanheiros = request.POST.get('Banheiros')
        propriedade.numero = request.POST.get('numero')
        propriedade.user = request.user
        propriedade.data = str(datetime.date.today())

        if len(request.FILES) != 0:
            propriedade.fotos = request.FILES['image']

        propriedade.save()
        return redirect('/plataforma/home')


@login_required(login_url='/auth/login')
def announce(request, id):
    if request.method == "GET":
        imoveis = reversed(Imovel_dois.objects.filter(id=id))
        comm = reversed(Comentarios.objects.filter(cids=id))
        context = {'imoveis': imoveis, 'user': request.user, 'comm': comm}
        print(comm)
        return render(request, 'announce.html', context)
    elif request.method == "POST":
        cmm = Comentarios()
        cmm.star = request.POST.get('select-star-rating')
        cmm.comments = request.POST.get('txt-avaliar')
        cmm.cids = id
        cmm.save()
        return render(request, 'home.html')


@login_required(login_url='/auth/login')
def share_home(request):
    if request.method == "GET":
        sh = Share.objects.all()
        context = {'sh': sh, 'user': request.user}
        return render(request, 'share_home.html', context)


@login_required(login_url='/auth/login')
def share_cad(request):
    if request.method == "POST":
        shr = Share()
        shr.numero = request.POST.get('contato')
        shr.descricao = request.POST.get('descricao')
        shr.uid = request.user
        shr.save()
        return render(request, 'share_cad.html')
    return render(request, 'share_cad.html')
