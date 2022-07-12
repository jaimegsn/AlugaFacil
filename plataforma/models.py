from django.db import models
from django.contrib.auth.models import User
import datetime
import os


# Bairro
# Descrição
# Valor
# Numero de Quartos
# Numero de Banheiros
# Multimidia
# Data

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Imovel_dois(models.Model):
    bairro = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField()
    nquartos = models.IntegerField()
    nbanheiros = models.IntegerField()
    data = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fotos = models.ImageField(upload_to=filepath, null=True, blank=True)
    numero = models.CharField(max_length=15)


class Comentarios(models.Model):
    comments = models.CharField(max_length=200)
    star = models.IntegerField()
    cids = models.IntegerField(null=True, blank=True)


class Share(models.Model):
    numero = models.CharField(max_length=15)
    descricao = models.CharField(max_length=200)
    user = models.CharField(max_length=100, null=True, blank=True)
